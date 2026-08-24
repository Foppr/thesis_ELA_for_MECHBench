import numpy as np

class HybridMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced polynomial base with higher-order terms and variable coefficients
        result = np.sum(0.3 * x**2 + 0.15 * x**3 + 0.03 * x**4 + 0.005 * x**5)
        
        # Stronger trigonometric coupling with multiple frequencies and amplitude modulation
        trig_term = np.sum(np.sin(3.0 * x) * np.cos(4.0 * x) * np.exp(-0.2 * np.abs(x)) * np.sin(0.5 * x))
        
        # Modified logarithmic barrier with sharper penalty near boundaries
        log_barrier = np.sum(np.log(1.0 + 0.5 * np.abs(x)) * np.exp(-0.1 * x**2) * np.cos(0.3 * x))
        
        # Asymmetric exponential decay with variable decay rates based on sign and magnitude
        asym_exp = np.sum(np.exp(-0.3 * x**2) * np.where(x >= 0, 1.2, 0.3) * np.sin(0.7 * x))
        
        # Coupled sine waves with dynamic phase shifts and frequency modulation
        phase_shifts = np.arange(self.dim) * np.pi / 3.0
        coupled_sine = np.sum(np.sin(x + phase_shifts) * np.cos(3.0 * x + phase_shifts) * np.exp(-0.15 * np.abs(x)))
        
        # Hyperbolic tangent with additional cosine modulation and adaptive strength
        tanh_mod = np.sum(np.tanh(x) * np.cos(0.8 * x) * np.exp(-0.3 * np.abs(x)) * (1.0 + 0.2 * np.sin(2.0 * x)))
        
        # Additional cubic coupling term between variables
        cubic_coupling = np.sum(x**3 * np.sin(0.5 * x) * np.exp(-0.1 * np.abs(x)))
        
        # Add all components together
        result = result + trig_term + log_barrier + asym_exp + coupled_sine + tanh_mod + cubic_coupling
        
        return result