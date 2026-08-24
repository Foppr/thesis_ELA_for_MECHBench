import numpy as np

class HybridMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Adaptive polynomial weights with modified scaling
        poly_weights = 0.3 + 0.7 * np.sin(0.5 * np.arange(self.dim))
        result = np.sum(poly_weights * (0.5 * x**2 + 0.2 * x**3 + 0.03 * x**4))
        
        # Enhanced chaotic sine-wave coupling with increased modulation
        freq_mod = 3.0 + 2.0 * np.sin(0.3 * np.arange(self.dim))
        chaotic_coupling = np.sum(np.sin(freq_mod * x) * np.cos(freq_mod * x + np.pi/4) * np.exp(-0.2 * np.abs(x)))
        
        # Modified hyperbolic secant barrier with sharper transition
        sec_barrier = np.sum(1.5 * (1.0 / np.cosh(1.5 * x)) * np.exp(-0.25 * x**2))
        
        # Adjusted asymmetric exponential with modified decay
        asym_exp = np.sum(np.exp(-0.5 * x**2) * np.where(x >= 0, 1.2, 0.3) * np.cos(0.4 * x))
        
        # Refined multi-scale coupled sine waves with phase locking
        phase_lock = np.sin(x + 0.3 * np.cos(x)) * np.cos(1.2 * x + 0.3 * np.sin(x))
        multi_scale = np.sum(phase_lock * np.exp(-0.2 * np.abs(x)))
        
        # Improved tanh modulation with frequency-dependent gain
        tanh_mod = np.sum(np.tanh(1.2 * x) * np.sin(0.9 * x) * np.exp(-0.25 * x**2))
        
        # Modified quadratic coupling with spatially varying coefficients
        spatial_coupling = np.sum((x[:-1] - x[1:]) ** 2 * np.exp(-0.1 * np.abs(x[:-1] + x[1:])))
        
        # Adjusted logistic map component for better complexity balance
        logistic_map = np.sum(3.8 * x * (1.0 - x) * np.exp(-0.1 * np.abs(x)))
        
        # Combine all components
        result = result + chaotic_coupling + sec_barrier + asym_exp + multi_scale + tanh_mod + spatial_coupling + logistic_map
        
        return result