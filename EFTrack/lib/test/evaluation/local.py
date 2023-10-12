from lib.test.evaluation.environment import EnvSettings

def local_env_settings():
    settings = EnvSettings()

    # Set your local paths here.

    settings.davis_dir = ''
    settings.got10k_lmdb_path = '/media/lw/C14D581BDA18EBFA/SeqTrack/data/got10k_lmdb'
    settings.got10k_path = '/media/lw/C14D581BDA18EBFA/SeqTrack/data/got10k'
    settings.got_packed_results_path = ''
    settings.got_reports_path = ''
    settings.lasot_extension_subset_path = '/media/lw/C14D581BDA18EBFA/SeqTrack/data/lasot_extension_subset'
    settings.lasot_lmdb_path = '/media/lw/C14D581BDA18EBFA/SeqTrack/data/lasot_lmdb'
    settings.lasot_path = '/media/lw/C14D581BDA18EBFA/SeqTrack/data/lasot'
    settings.network_path = '/media/lw/C14D581BDA18EBFA/SeqTrack/test/networks'    # Where tracking networks are stored.
    settings.nfs_path = '/media/lw/C14D581BDA18EBFA/SeqTrack/data/nfs'
    settings.otb_path = '/media/lw/C14D581BDA18EBFA/SeqTrack/data/OTB2015'
    settings.prj_dir = '/media/lw/C14D581BDA18EBFA/SeqTrack'
    settings.result_plot_path = '/media/lw/C14D581BDA18EBFA/SeqTrack/test/result_plots'
    settings.results_path = '/media/lw/C14D581BDA18EBFA/SeqTrack/test/tracking_results'    # Where to store tracking results
    settings.save_dir = '/media/lw/C14D581BDA18EBFA/SeqTrack'
    settings.segmentation_path = '/media/lw/C14D581BDA18EBFA/SeqTrack/test/segmentation_results'
    settings.tc128_path = '/media/lw/C14D581BDA18EBFA/SeqTrack/data/TC128'
    settings.tn_packed_results_path = ''
    settings.tnl2k_path = '/media/lw/C14D581BDA18EBFA/SeqTrack/data/tnl2k'
    settings.tpl_path = ''
    settings.trackingnet_path = '/media/lw/C14D581BDA18EBFA/SeqTrack/data/trackingnet'
    settings.uav_path = '/media/lw/C14D581BDA18EBFA/SeqTrack/data/UAV123'
    settings.vot_path = '/media/lw/C14D581BDA18EBFA/SeqTrack/data/VOT2019'
    settings.youtubevos_dir = ''

    return settings

