# vim: set fileencoding=utf-8
from typing import Any, Dict, Tuple

from bemani.backend.popn.base import PopnMusicBase
from bemani.backend.popn.common import PopnMusicModernBase
from bemani.backend.popn.eclale import PopnMusicEclale
from bemani.common import VersionConstants


class PopnMusicUsaNeko(PopnMusicModernBase):

    name: str = "Pop'n Music うさぎと猫と少年の夢"
    version: int = VersionConstants.POPN_MUSIC_USANEKO

    # Biggest ID in the music DB
    GAME_MAX_MUSIC_ID: int = 1704

    def previous_version(self) -> PopnMusicBase:
        return PopnMusicEclale(self.data, self.config, self.model)

    @classmethod
    def get_settings(cls) -> Dict[str, Any]:
        """
        Return all of our front-end modifiably settings.
        """
        return {
            'ints': [
                {
                    'name': 'Music Open Phase',
                    'tip': 'Default music phase for all players.',
                    'category': 'game_config',
                    'setting': 'music_phase',
                    'values': {
                        0: 'No music unlocks',
                        1: 'Phase 1',
                        2: 'Phase 2',
                        3: 'Phase 3',
                        4: 'Phase 4',
                        5: 'Phase 5',
                        6: 'Phase 6',
                        7: 'Phase 7',
                        8: 'Phase 8',
                        9: 'Phase 9',
                        10: 'Phase 10',
                        11: 'Phase MAX',
                    }
                },
                {
                    'name': 'Active Event',
                    'tip': 'Active event for all players.',
                    'category': 'game_config',
                    'setting': 'active_event',
                    'values': {
                        0: 'No event',
                        1: 'NAVI-Kun event',
                        2: 'Daily Mission event',
                    },
                },
                {
                    'name': 'NAVI-Kun Event Phase',
                    'tip': 'NAVI-Kun event phase for all players.',
                    'category': 'game_config',
                    'setting': 'navikun_phase',
                    'values': {
                        0: 'Phase 1',
                        1: 'Phase 2',
                        2: 'Phase 3',
                        3: 'Phase 4',
                        4: 'Phase 5',
                        5: 'Phase 6',
                        6: 'Phase 7',
                        7: 'Phase 8',
                        8: 'Phase 9',
                        9: 'Phase 10',
                        10: 'Phase 11',
                        11: 'Phase 12',
                        12: 'Phase 13',
                        13: 'Phase 14',
                        14: 'Phase 15',
                        15: 'Phase MAX',
                    },
                },
            ],
            'bools': [
                {
                    'name': 'Force Song Unlock',
                    'tip': 'Force unlock all songs.',
                    'category': 'game_config',
                    'setting': 'force_unlock_songs',
                },
            ],
        }

    def get_common_config(self) -> Tuple[Dict[int, int], bool]:
        game_config = self.get_game_config()
        music_phase = game_config.get_int('music_phase')
        active_event = game_config.get_int('active_event')
        navikun_phase = game_config.get_int('navikun_phase')

        navikun_enabled = active_event == 1
        daily_mission_enabled = active_event == 2

        # Event phases
        return (
            {
                # Default song phase availability (0-11)
                # The following songs are unlocked when the phase is at or above the number specified:
                # 1  - 1589, 1590, 1591
                # 2  - 1594, 1595
                # 3  - 1596, 1597
                # 4  - 1593
                # 5  - 1602
                # 6  - 1604
                # 7  - 1629, 1630, 1631, 1633, 1641, 1642, 1643, 1644, 1645, 1646, 1647
                # 8  - 1632
                # 9  - 1651
                # 10 - 1679, 1680, 1681
                # 11 - 1669, 1670, 1669, 1670
                0: music_phase,
                # Unknown event (0-2)
                1: 2,
                # Unknown event (0-2)
                2: 2,
                # Unknown event (0-4)
                3: 4,
                # Unknown event (0-1)
                4: 1,
                # Enable Net Taisen, including win/loss display on song select (0-1)
                5: 1,
                # Enable NAVI-kun shunkyoku toujou, allows song 1608 to be unlocked (0-1)
                6: 1,
                # Unknown event (0-1)
                7: 1,
                # Unknown event (0-2)
                8: 2,
                # Daily Mission (0-2)
                9: 2 if daily_mission_enabled else 0,
                # NAVI-kun Song phase availability (0-15)
                # The following songs are unlocked when the phase is at or above the number specified:
                # 1  - 1553
                # 2  - 1577, 1576, 1569
                # 3  - 1575, 1557
                # 4  - 1567
                # 5  - 1587, 1588, 1585
                # 6  - 1586
                # 7  - 1601, 1600, 1599
                # 8  - 1603
                # 9  - 1606, 1607, 1605
                # 10 - 1610, 1611, 1612
                # 11 - 1616, 1613, 1614, 1615
                # 12 - 1619, 1618, 1620, 1617
                # 13 - 1624, 1621, 1623, 1622
                # 14 - 1627, 1626, 1625
                # 15 - 1628
                10: navikun_phase,
                # Unknown event (0-1)
                11: 1,
                # Unknown event (0-2)
                12: 2,
                # Enable Pop'n Peace preview song (1703) (0-1)
                13: 1,
            },
            navikun_enabled,
        )
