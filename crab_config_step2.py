from CRABClient.UserUtilities import config
config = config()
config.JobType.allowUndistributedCMSSW = True
config.General.requestName = 'Higgs_scalar_nohdecay_gg_1GeV_13TeV_RECO_v3'
config.General.workArea = 'crab_projects'

config.JobType.pluginName = 'Analysis'
#config.JobType.generator = 'lhe'
config.JobType.psetName = 'step2.py'
config.Data.inputDataset = '/MinBias/soffi-Higgs_scalar_nohdecay_gg_1GeV_13TeV-a3a9f79104271b5b0a2231156aced621/USER'
config.Data.inputDBS = 'phys03'
config.Data.ignoreLocality = True
config.Site.whitelist = ["T2_IT_Rome"]
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 10
NJOBS = 10
config.Data.totalUnits = config.Data.unitsPerJob * NJOBS
config.Data.outLFNDirBase = '/store/user/soffi/' # or '/store/group/<subdir>'
config.Data.publication = True
config.Data.publishDataName = 'Higgs_scalar_nohdecay_gg_1GeV_13TeV_RECO_v3'
#config.Data.userInputFiles = list(open('Higgs_scalar_nohdecay_gg_1GeV_13TeV_v1.txt'))
config.section_('User')
config.section_('Site')
config.Site.storageSite = 'T2_IT_Rome'
