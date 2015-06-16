from CRABClient.UserUtilities import config
config = config()

config.General.requestName = 'Higgs_scalar_nohdecay_gg_1GeV_13TeV_MINIAODSIM_v3'
config.General.workArea = 'crab_projects'

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'step3.py'
config.Data.inputDataset = '/MinBias/soffi-Higgs_scalar_nohdecay_gg_1GeV_13TeV_RECO_v3-9c909acf833da182901392c6a5ed5f18/USER'
config.Data.inputDBS = 'phys03'
config.Data.ignoreLocality = True
config.Site.whitelist = ["T2_IT_Rome"]
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
NJOBS = 10
config.Data.totalUnits = config.Data.unitsPerJob * NJOBS
config.Data.outLFNDirBase = '/store/user/soffi/' # or '/store/group/<subdir>'
config.Data.publication = True
config.Data.publishDataName = 'Higgs_scalar_nohdecay_gg_1000GeV_13TeV_AODSIM_v3'
#config.Data.userInputFiles = list(open('Higgs_hzpzp_nohdecay_ww_1000GeV_13TeV_RECO_v1.txt'))
config.section_('User')
config.section_('Site')

config.Site.storageSite = 'T2_IT_Rome'
