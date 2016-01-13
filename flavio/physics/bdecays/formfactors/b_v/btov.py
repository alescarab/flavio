from flavio.physics.bdecays.formfactors.b_v import bsz
from flavio.physics.bdecays.formfactors.common import FormFactorParametrization

FFs = ["A0","A1","A12","V","T1","T2","T23"]

bsz_parnames = [ ff + '_' + a for ff in FFs for a in ["a0","a1","a2"]]
bsz_processes = ['B->K*','B->rho','B->omega','Bs->phi','Bs->K*']

bsz2 = FormFactorParametrization(name='bsz2',
                                 transition='b_v',
                                 processes=bsz_processes,
                                 parameters=bsz_parnames,
                                 function=lambda process, q2, par: bsz.ff(process, q2, par, n=1))

bsz3 = FormFactorParametrization(name='bsz3',
                                 transition='b_v',
                                 processes=bsz_processes,
                                 parameters=bsz_parnames,
                                 function=lambda process, q2, par: bsz.ff(process, q2, par, n=2))