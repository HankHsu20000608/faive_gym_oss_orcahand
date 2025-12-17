from isaacgym import gymapi

gym = gymapi.acquire_gym()
sim_params = gymapi.SimParams()
sim = gym.create_sim(0, 0, gymapi.SIM_PHYSX, sim_params)

asset_root = "/home/fw3/Desktop/orca_hand/faive_gym_oss/assets"
asset_file = "orcahand/models/urdf/orcahand_right.urdf"

asset_opts = gymapi.AssetOptions()
asset = gym.load_asset(sim, asset_root, asset_file, asset_opts)

print("Rigid bodies:")
for i in range(gym.get_asset_rigid_body_count(asset)):
    print(i, gym.get_asset_rigid_body_name(asset, i))

"""
dof_count: 17
body_count: 42
0 right_wrist driveMode= 0
1 right_index_abd driveMode= 0
2 right_index_mcp driveMode= 0
3 right_index_pip driveMode= 0
4 right_middle_abd driveMode= 0
5 right_middle_mcp driveMode= 0
6 right_middle_pip driveMode= 0
7 right_pinky_abd driveMode= 0
8 right_pinky_mcp driveMode= 0
9 right_pinky_pip driveMode= 0
10 right_ring_abd driveMode= 0
11 right_ring_mcp driveMode= 0
12 right_ring_pip driveMode= 0
13 right_thumb_mcp driveMode= 0
14 right_thumb_abd driveMode= 0
15 right_thumb_pip driveMode= 0
16 right_thumb_dip driveMode= 0

Rigid bodies:
0 world
1 world2right_tower_fixed_jointbody
2 right_tower
3 right_wrist_jointbody
4 right_palm
5 right_index_abd_jointbody
6 right_index_mp
7 right_index_mcp_jointbody
8 right_index_pp
9 right_index_pip_jointbody
10 right_index_ip
11 right_index_fingertip
12 right_middle_abd_jointbody
13 right_middle_mp
14 right_middle_mcp_jointbody
15 right_middle_pp
16 right_middle_pip_jointbody
17 right_middle_ip
18 right_middle_fingertip
19 right_pinky_abd_jointbody
20 right_pinky_mp
21 right_pinky_mcp_jointbody
22 right_pinky_pp
23 right_pinky_pip_jointbody
24 right_pinky_ip
25 right_pinky_fingertip
26 right_ring_abd_jointbody
27 right_ring_mp
28 right_ring_mcp_jointbody
29 right_ring_pp
30 right_ring_pip_jointbody
31 right_ring_ip
32 right_ring_fingertip
33 right_thumb_mcp_jointbody
34 right_thumb_mp
35 right_thumb_abd_jointbody
36 right_thumb_pp
37 right_thumb_pip_jointbody
38 right_thumb_ip
39 right_thumb_dip_jointbody
40 right_thumb_dp
41 right_thumb_fingertip

"""