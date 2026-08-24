import numpy as np

class HybridMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced polynomial base with increased nonlinearity
        result = np.sum(0.5 * x**2 + 0.2 * x**3 + 0.02 * x**4)
        
        # Stronger trigonometric coupling with frequency modulation
        trig_term = np.sum(np.sin(4.0 * x) * np.cos(5.0 * x) * np.exp(-0.2 * np.abs(x)))
        
        # Reinforced logarithmic barrier with sharper penalty
        log_barrier = np.sum(2.0 * np.log(1.0 + 0.5 * np.abs(x)) * np.exp(-0.15 * x**2))
        
        # Asymmetric exponential decay with amplified scaling
        asym_exp = np.sum(np.exp(-0.4 * x**2) * np.where(x >= 0, 1.5, 0.2))
        
        # Coupled sine waves with randomized phase shifts for increased complexity
        phase_shifts = np.random.RandomState(42).random(self.dim) * np.pi
        coupled_sine = np.sum(np.sin(x + phase_shifts) * np.cos(2.5 * x + phase_shifts))
        
        # Hyperbolic tangent modulation with stronger interaction
        tanh_mod = np.sum(np.tanh(1.5 * x) * np.sin(0.5 * x) * np.exp(-0.3 * np.abs(x)))
        
        # Additional quadratic coupling term for increased conditioning
        quad_coupling = np.sum((x[:-1] - x[1:]) ** 2 * np.exp(-0.1 * np.abs(x[:-1])))
        
        # Combine all components
        result = result + trig_term + log_barrier + asym_exp + coupled_sine + tanh_mod + quad_coupling
        
        return result