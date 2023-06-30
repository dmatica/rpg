import sys
import pandas as pd
from lxml import etree
import clipboard
import datetime

lstkey=[]
lstval=[]
runID=''
fc_ser=''
fc_lot=''
fc_exp=''
fc_mod=''
fc_part=''
fc_type=''
pr_ser=''
pr_lot=''
pr_exp=''
rg_ser=''
rg_lot=''
rg_exp=''
rg_part=''
rg_type=''
ce_ser=''
ce_lot=''
ce_exp=''
instr=''
runstartdate=''
w=''
x=''
y=''
z=''
workflow=''
custom=''
r1=''
r2=''
i1=''
i2=''

data = '/Users/davindersandhu/PycharmProjects/pythonProject/RunParameters.xml'
#data = sys.argv[1]#+"/RunParameters.xml"
tree = etree.parse(data)
for p in tree.iter():
    lstkey.append(tree.getpath(p).replace("/",".")[1:])
    lstval.append(p.text)
df = pd.DataFrame({'key':lstkey, 'value':lstval})

for i in range(0,len(df)):
    ##print(df.key[i])
    #runstartdate
    if df.key[i].lower()=='runparameters.runstartdate' and len(df.value[i])<7:
        runstartdate=pd.to_datetime(df.value[i],format='%y%m%d').strftime('%d-%b-%Y').upper()
    elif df.key[i].lower() == 'runparameters.runstartdate' and len(df.value[i])>7:
        runstartdate=pd.to_datetime(df.value[i].split(' ',1)[0],format='%Y/%m/%d').strftime('%d-%b-%Y').upper()
    elif df.key[i].lower()=='runparameters.runstarttime':
        runstartdate=pd.to_datetime(df.value[i].split(' ',1)[0],format='%Y/%m/%d').strftime('%d-%b-%Y').upper()
    #instrumenttype
    if df.key[i].lower()=='runparameters.setup.applicationname':
        instr=df.value[i].lower()
    elif df.key[i].lower()=='runparameters.applicationname':
        instr = df.value[i].lower()
    elif df.key[i].lower()=='runparameters.application':
        instr = df.value[i].lower()

    #runID
    if df.key[i].lower()=='runparameters.runid':
        runID = df.value[i]
    elif df.key[i].lower()=='runparameters.plannedrunid':
        runID = df.value[i]

    #FlowCell
    if df.key[i].lower()=='runparameters.flowcellrfidtag.serialnumber':
        fc_ser=df.value[i]
    if df.key[i].lower()=='runparameters.flowcellrfidtag.lotnumber':
        fc_lot=df.value[i]
    if df.key[i].lower()=='runparameters.flowcellrfidtag.expirationdate':
        fc_exp=pd.to_datetime(df.value[i],format='%Y-%m-%d').strftime('%d-%b-%Y').upper()
    if df.key[i].lower()=='runparameters.flowcellrfidtag.partnumber':
        fc_part=df.value[i]
    #FC-iSeq
    if df.key[i].lower()=='runparameters.flowcelleepromtag.serialnumber':
        fc_ser=df.value[i]
    if df.key[i].lower()=='runparameters.flowcelleepromtag.lotnumber':
        fc_lot=df.value[i]
    if df.key[i].lower()=='runparameters.flowcelleepromtag.expirationdate':
        fc_exp=pd.to_datetime(df.value[i],format='%Y-%m-%d').strftime('%d-%b-%Y').upper()
    if df.key[i].lower()=='runparameters.flowcelleepromtag.partnumber':
        fc_part=df.value[i]
    #FC-N2k
    if df.key[i].lower()=='runparameters.flowcellserialnumber':
        fc_ser=df.value[i]
    if df.key[i].lower()=='runparameters.flowcelllotnumber':
        fc_lot=df.value[i]
    if df.key[i].lower()=='runparameters.flowcellexpirationdate':
        fc_exp = pd.to_datetime(df.value[i], format='%m/%d/%Y').strftime('%d-%b-%Y').upper()
    if df.key[i].lower()=='runparameters.flowcellpartnumber':
        fc_part=df.value[i]
    #FC-Nova
    if df.key[i].lower()=='runparameters.rfidsinfo.flowcellserialbarcode':
        fc_ser=df.value[i]
    if df.key[i].lower()=='runparameters.rfidsinfo.flowcelllotnumber':
        fc_lot=df.value[i]
    if df.key[i].lower()=='runparameters.rfidsinfo.flowcellexpirationdate':
        fc_exp=pd.to_datetime(df.value[i].split(' ',1)[0],format='%m/%d/%Y').strftime('%d-%b-%Y').upper()
    if df.key[i].lower()=='runparameters.rfidsinfo.flowcellmode':
        fc_mod=df.value[i]
    if df.key[i].lower()=='runparameters.rfidsinfo.flowcellpartnumber':
        fc_part=df.value[i]
    #FC-NovaX
    if df.key[i].lower()=='runparameters.consumableinfo.consumableinfo[1].serialnumber':
        fc_ser=df.value[i]
        if runID[:3]=="202":
            runstartdate=str(pd.to_datetime(runID[:8],format='%Y%m%d').strftime('%d-%b-%Y').upper())
    if df.key[i].lower()=='runparameters.consumableinfo.consumableinfo[1].lotnumber':
        fc_lot=df.value[i]
    if df.key[i].lower()=='runparameters.consumableinfo.consumableinfo[1].expirationdate':
        fc_exp=pd.to_datetime(df.value[i], format='%Y-%m-%d').strftime('%d-%b-%Y').upper()
    if df.key[i].lower()=='runparameters.consumableinfo.consumableinfo[1].mode':
        fc_mod=df.value[i]
    if df.key[i].lower()=='runparameters.consumableinfo.consumableinfo[1].partnumber':
        fc_part=df.value[i]
    #PR-2/Buffer bottle
    if df.key[i].lower()=='runparameters.pr2bottlerfidtag.serialnumber':
        pr_ser=df.value[i]
    if df.key[i].lower()=='runparameters.pr2bottlerfidtag.lotnumber':
        pr_lot=df.value[i]
    if df.key[i].lower()=='runparameters.pr2bottlerfidtag.expirationdate':
        pr_exp=pd.to_datetime(df.value[i], format='%Y-%m-%d').strftime('%d-%b-%Y').upper()
    #PR-2/Buffer Nova
    if df.key[i].lower()=='runparameters.rfidsinfo.bufferserialbarcode':
        pr_ser=df.value[i]
    if df.key[i].lower()=='runparameters.rfidsinfo.bufferlotnumber':
        pr_lot=df.value[i]
    if df.key[i].lower()=='runparameters.rfidsinfo.bufferexpirationdate':
        pr_exp=pd.to_datetime(df.value[i].split(' ',1)[0],format='%m/%d/%Y').strftime('%d-%b-%Y').upper()
    #Buffer NovaX
    if df.key[i].lower()=='runparameters.consumableinfo.consumableinfo[3].serialnumber':
        pr_ser=df.value[i]
    if df.key[i].lower()=='runparameters.consumableinfo.consumableinfo[3].lotnumber':
        pr_lot=df.value[i]
    if df.key[i].lower()=='runparameters.consumableinfo.consumableinfo[3].expirationdate':
        pr_exp=pd.to_datetime(df.value[i], format='%Y-%m-%d').strftime('%d-%b-%Y').upper()

    #Reagent kit
    if df.key[i].lower()=='runparameters.reagentkitrfidtag.serialnumber':
        rg_ser=df.value[i]
    if df.key[i].lower()=='runparameters.reagentkitrfidtag.lotnumber':
        rg_lot=df.value[i]
    if df.key[i].lower()=='runparameters.reagentkitrfidtag.expirationdate':
        rg_exp=pd.to_datetime(df.value[i], format='%Y-%m-%d').strftime('%d-%b-%Y').upper()
    if df.key[i].lower()=='runparameters.reagentkitrfidtag.partnumber':
        rg_part=df.value[i]
    #Reagent N2K
    if df.key[i].lower()=='runparameters.cartridgeserialnumber':
        rg_ser=df.value[i]
    if df.key[i].lower()=='runparameters.cartridgelotnumber':
        rg_lot=df.value[i]
    if df.key[i].lower()=='runparameters.cartridgeexpirationdate':
        rg_exp=pd.to_datetime(df.value[i], format='%m/%d/%Y').strftime('%d-%b-%Y').upper()
    if df.key[i].lower()=='runparameters.cartridgepartnumber':
        rg_part=df.value[i]
    #Reagent Nova
    if df.key[i].lower()=='runparameters.rfidsinfo.sbsserialbarcode':
        rg_ser=df.value[i]
    if df.key[i].lower()=='runparameters.rfidsinfo.sbslotnumber':
        rg_lot=df.value[i]
    if df.key[i].lower()=='runparameters.rfidsinfo.sbsexpirationdate':
        rg_exp=pd.to_datetime(df.value[i].split(' ',1)[0],format='%m/%d/%Y').strftime('%d-%b-%Y').upper()
    if df.key[i].lower()=='runparameters.rfidsinfo.sbspartnumber':
        rg_part=df.value[i]
    #Reagent NovaX
    if df.key[i].lower()=='runparameters.consumableinfo.consumableinfo[2].serialnumber':
        rg_ser=df.value[i]
    if df.key[i].lower()=='runparameters.consumableinfo.consumableinfo[2].lotnumber':
        rg_lot=df.value[i]
    if df.key[i].lower()=='runparameters.consumableinfo.consumableinfo[2].expirationdate':
        rg_exp=pd.to_datetime(df.value[i], format='%Y-%m-%d').strftime('%d-%b-%Y').upper()

    #Clusterkit Nova
    if df.key[i].lower()=='runparameters.rfidsinfo.clusterserialbarcode':
        ce_ser=df.value[i]
    if df.key[i].lower()=='runparameters.rfidsinfo.clusterlotnumber':
        ce_lot=df.value[i]
    if df.key[i].lower()=='runparameters.rfidsinfo.clusterexpirationdate':
        ce_exp=pd.to_datetime(df.value[i].split(' ',1)[0],format='%m/%d/%Y').strftime('%d-%b-%Y').upper()

    #Nova workflow
    if df.key[i].lower()=='runparameters.workflowtype':
        #print(df.key[i])
        workflow = "Workflow: "+df.value[i]
    if df.key[i].lower()=='runparameters.clouduploadmode':
        workflow = "Workflow: "+df.value[i]

    #Custom primers
    if (df.key[i].lower() == 'runparameters.usescustomreadoneprimer' and df.value[i].lower()=='true') or (df.key[i].lower()=='runparameters.usecustomread1primer' and df.value[i].lower()=='true'):
        r1=True
        custom=custom+"read1 "
    if (df.key[i].lower() == 'runparameters.usescustomreadtwoprimer' and df.value[i].lower()=='true') or (df.key[i].lower()=='runparameters.usecustomread2primer' and df.value[i].lower()=='true'):
        r2 = True
        custom=custom+"read2 "
    if (df.key[i].lower() == 'runparameters.usescustomindexprimer' and df.value[i].lower()=='true') or (df.key[i].lower()=='runparameters.usecustomindexread1primer' and df.value[i].lower()=='true'):
        i1 = True
        custom=custom+"index1 "
    if df.key[i].lower() == 'runparameters.usescustomindextwoprimer' and df.value[i].lower()=='true':
        i2 = True
        custom=custom+"index2 "

kit=''
k1=''
k2=''
#print(type(fc_part))
if (rg_part!='') or (fc_part!=''):
    bom = pd.read_csv("/Users/davindersandhu/PycharmProjects/pythonProject/RPG_bom.csv")
    for i in range(1,len(bom)):
        #print(type(bom.at[i,'number']))
        if fc_part == str(bom.at[i,'number']):
            #print(bom.at[i,'number'])
            k1 = str(bom.at[i,'part'])
        if rg_part == str(bom.at[i,'number']):
            k2 = str(bom.at[i,'part'])
    if k1 =='':
        k1 = "Unknown flow cell type"
    if k2 =='':
        k2 = "Unknown reagent kit type"
    kit = "("+k1+" + "+k2+")"

if custom != '':
    custom = "Uses custom: "+custom+"primers"

#print(instr.split(' ',1)[0])
#output
v=("RunID: "+runID)
if fc_lot=='':
    print(runstartdate,fc_exp)
    if runstartdate == '':
        fc_exp = str(fc_exp)
    elif datetime.datetime.strptime(runstartdate, '%d-%b-%Y') > datetime.datetime.strptime(fc_exp, '%d-%b-%Y'):
        fc_exp = fc_exp+" --> EXPIRED at time of run"
    w=("FC: serial = " + fc_ser + ", exp = " + fc_exp)
    if pr_ser != '':
        if datetime.datetime.strptime(runstartdate, '%d-%b-%Y') > datetime.datetime.strptime(pr_exp, '%d-%b-%Y'):
            pr_exp = pr_exp + " --> EXPIRED at time of run"
        x=("PR2Buffer: serial = " + pr_ser + ", exp = " + pr_exp)
    if datetime.datetime.strptime(runstartdate, '%d-%b-%Y') > datetime.datetime.strptime(rg_exp, '%d-%b-%Y'):
        rg_exp = rg_exp+" --> EXPIRED at time of run"
    y=("Reagentkit: serial = " + rg_ser + ", exp = " + rg_exp)
else:
    if runstartdate == '':
        fc_exp = str(fc_exp)
    elif datetime.datetime.strptime(runstartdate, '%d-%b-%Y') > datetime.datetime.strptime(fc_exp, '%d-%b-%Y'):
        fc_exp = fc_exp+" --> EXPIRED at time of run"
    w=("FC: serial = " + fc_ser + ", lot = " + fc_lot + ", exp = " + fc_exp)
    if pr_ser!='':
        if runstartdate=='':
            pr_exp=str(pr_exp)
        elif datetime.datetime.strptime(runstartdate, '%d-%b-%Y') > datetime.datetime.strptime(pr_exp, '%d-%b-%Y'):
            pr_exp = pr_exp + " --> EXPIRED at time of run"
        x=("PR2Buffer: serial = "+pr_ser+", lot = "+pr_lot+", exp = "+pr_exp)
    if rg_exp!='':
        if runstartdate=='':
            rg_exp=str(rg_exp)
        elif datetime.datetime.strptime(runstartdate, '%d-%b-%Y') > datetime.datetime.strptime(rg_exp, '%d-%b-%Y'):
            rg_exp = rg_exp+" --> EXPIRED at time of run"
    y=("Reagentkit: serial = "+rg_ser+", lot = "+rg_lot+", exp = "+rg_exp)
    if instr.split(' ', 1)[0].lower() == "novaseq":
        if datetime.datetime.strptime(runstartdate, '%d-%b-%Y') > datetime.datetime.strptime(ce_exp, '%d-%b-%Y'):
            ce_exp = ce_exp + " --> EXPIRED at time of run"
        z=("Cluster: serial = "+ce_ser+", lot= "+ce_lot+", exp = "+ce_exp)
print(z, custom)
if pr_ser!='':
    if custom != '' and z!= '':
        clipboard.copy("\n".join([v, kit, w, x, y, z, custom, workflow]).strip())
    elif custom != '' and z== '':
        clipboard.copy("\n".join([v, kit, w, x, y, custom, workflow]).strip())
    else:
        clipboard.copy("\n".join([v, kit, w, x, y, z, workflow]).strip())
else:
    clipboard.copy("\n".join([v,kit,w,y,custom]).strip())