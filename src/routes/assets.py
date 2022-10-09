from flask import Blueprint, send_from_directory

assets = Blueprint('assets', __name__, url_prefix='/assets')


@assets.route('/<string:asset_id>', methods=['GET'])
def get_assets(asset_id):
    return send_from_directory('assets', asset_id)
