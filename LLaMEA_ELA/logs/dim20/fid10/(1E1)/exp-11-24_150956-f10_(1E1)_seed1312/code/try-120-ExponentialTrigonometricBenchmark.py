import numpy as np

class ExponentialTrigonometricBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Exponential decay components with varying rates and amplitudes
        exp_terms = np.sum(0.7 * np.exp(-3.0 * np.abs(x_scaled)) + 
                          0.3 * np.exp(-5.0 * np.abs(x_scaled)) + 
                          0.2 * np.exp(-2.0 * np.abs(x_scaled)))
        
        # Trigonometric interference with multiple frequencies and phase shifts
        trig_terms = np.sum(np.sin(8.0 * x_scaled) * np.cos(6.0 * x_scaled) + 
                           0.5 * np.sin(12.0 * x_scaled**2) * np.cos(10.0 * x_scaled**2) + 
                           0.3 * np.sin(15.0 * x_scaled**3) * np.cos(13.0 * x_scaled**3))
        
        # Polynomial coupling with asymmetric weights
        poly_coupling = np.sum((x_scaled[:-1]**3 + x_scaled[1:]**3) * 
                             np.sin(2.0 * (x_scaled[:-1] - x_scaled[1:])) + 
                             (x_scaled[:-2]**4 + x_scaled[2:]**4) * 
                             np.cos(3.0 * (x_scaled[:-2] + x_scaled[2:])))
        
        # Asymmetric exponential interaction with cross-dimensional coupling
        asym_exp = np.sum(np.exp(-1.5 * (x_scaled**2 + 0.5 * x_scaled**4)) * 
                         (1.0 + 0.3 * np.sin(5.0 * x_scaled)))
        
        # Weighted sum with non-uniform coefficients
        return 0.4 * exp_terms + 0.35 * trig_terms + 0.15 * poly_coupling + 0.1 * asym_exp + 2.1