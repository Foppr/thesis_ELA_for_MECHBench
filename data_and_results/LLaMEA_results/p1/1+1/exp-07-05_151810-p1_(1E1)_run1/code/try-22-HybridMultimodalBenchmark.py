import numpy as np

class HybridMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial base with altered weights for increased conditioning
        result = np.sum(0.3 * x**2 + 0.15 * x**3 + 0.05 * x**4)
        
        # Trigonometric components with modified frequencies
        trig_term = np.sum(np.sin(3.0 * x) * np.cos(4.0 * x) * np.exp(-0.15 * np.abs(x)))
        
        # Logarithmic barrier terms with stronger penalty near boundaries
        log_barrier = np.sum(1.5 * np.log(1.0 + np.abs(x)) * np.exp(-0.1 * x**2))
        
        # Asymmetric exponential decay with modified scaling
        asym_exp = np.sum(np.exp(-0.3 * x**2) * np.where(x >= 0, 1.2, 0.3))
        
        # Coupled sine waves with different phase shifts
        phase_shifts = np.arange(self.dim) * np.pi / 6.0
        coupled_sine = np.sum(np.sin(x + phase_shifts) * np.cos(3.0 * x + phase_shifts))
        
        # Hyperbolic tangent modulation with adjusted strength
        tanh_mod = np.sum(np.tanh(x) * np.sin(0.3 * x) * np.exp(-0.25 * np.abs(x)))
        
        # Add all components together
        result = result + trig_term + log_barrier + asym_exp + coupled_sine + tanh_mod
        
        return result