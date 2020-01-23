import httpx


class Unified:
    '''Unified REST API

    A random assortment of URLs
    '''
    defaults = {
        'unified_base': 'https://cms-unified.web.cern.ch/cms-unified/',
    }

    @classmethod
    def add_args(cls, parser):
        group = parser.add_argument_group('Unified API config')
        group.add_argument(
            '--unified_base',
            default=cls.defaults['unified_base'],
            help='Unified base URL with trailing slash (default: %(default)s)',
        )
        return group

    @classmethod
    def from_cli(cls, client, args):
        return cls(
            client,
            unified_base=args.unified_base,
        )

    def __init__(self, client, **kwargs):
        args = dict(Unified.defaults)
        args.update(kwargs)
        self.client = client
        self.baseurl = httpx.URL(args['unified_base'])

    async def transfer_statuses(self):
        res = await self.client.getjson(
            url=self.baseurl.join('transfer_statuses.json'),
        )
        return res
