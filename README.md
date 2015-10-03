# MCProduction13TeV

Produce Locally:
-----------------------------------------------------
    STEP1((GEN,SIM,DIGI,L1,DIGI2RAW,HLT+PU))
    ***cmsDriver.py Hadronizer_MgmMatchTune4C_13TeV_madgraph_pythia8_Tauola_cff.py 
    --filein file:events.lhe --mc --pileup_input 
    dbs:/MinBias_TuneA2MB_13TeV-pythia8/Fall13-POSTLS162_V1-v1/GEN-SIM 
    --eventcontent RAWSIM --pileup AVE_40_BX_25ns --datatier GEN-SIM-RAW
    --customise SLHCUpgradeSimulations /Configuration/postLS1Customs.customisePostLS1,Configuration/DataProcessing/Utils.addMonitoring --conditions PHYS14_25_V1 --magField 38T_PostLS1 --step GEN,SIM,DIGI,L1,DIGI2RAW,HLT:GRun --no_exec -n 10 --python_filename step1_new.py --fileout file:step1.root
    
    ***Modify the step1.root and add the decay of the Higgs:

    PythiaParameters = cms.PSet(
            processParameters = cms.vstring('Main:timesAllowErrors = 10000',
                'ParticleDecays:limitTau0 = on',
                'ParticleDecays:tauMax = 10',
                'Tune:ee 3',
                'Tune:pp 5',
                <span class="WYSIWYG_TT"><i>'25:onMode = off',</i></span>
    <span class="WYSIWYG_TT"><i>            '25:onIfAll = 22 22',</i></span>
    <span class="WYSIWYG_TT"><i>            'SLHA:keepSM = on',</i></span>
    <span class="WYSIWYG_TT"><i>            'SLHA:minMassSM = 1000.',</i></span>
    <span class="WYSIWYG_TT"><i>            'SLHA:useDecayTable = off'</i></span>),
            parameterSets = cms.vstring('processParameters')
        )

    ***cmsRun step1.py 
    
   -------------------------------------------------------------
 
    STEP2 (RECO)
    ***cmsDriver.py step2 --filein file:step1.root --fileout file:step2.root 
    --mc --eventcontent AODSIM --customise 
    SLHCUpgradeSimulations/Configuration/postLS1Customs.customisePostLS1,Configuration/DataProcessing/Utils.addMonitoring --datatier AODSIM --conditions PHYS14_25_V1 --step RAW2DIGI,L1Reco,RECO --magField 38T_PostLS1 --python_filename step2.py -n 10 

    -------------------------------------------------------------
    STEP3 (MINIAOD) 
    
    ***cmsDriver.py step3 --filein file:step2.root --fileout file:step3.root --mc
    --eventcontent MINIAODSIM --runUnscheduled --datatier MINIAODSIM 
    --conditions PHYS14_25_V1 --step PAT --python_filename step3.py 
    --customise Configuration/DataProcessing/Utils.addMonitoring -n 10 


//ciao!