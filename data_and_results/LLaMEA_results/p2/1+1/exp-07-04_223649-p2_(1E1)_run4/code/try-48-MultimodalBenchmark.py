import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic component
        result = np.sum(x**2)
        
        # Chaotic tent map perturbations with varying parameter
        tent_pert = 0.0
        for i in range(self.dim):
            if x[i] < 0.5:
                tent_val = 2.0 * x[i]
            else:
                tent_val = 2.0 * (1.0 - x[i])
            tent_pert += tent_val * np.sin(3.0 * np.pi * x[i])
        result += 0.8 * tent_pert
        
        # Enhanced trigonometric coupling with adaptive frequencies
        trig_coupling = 0.0
        for i in range(self.dim - 1):
            freq_i = 1.0 + 0.5 * np.sin(x[i])
            freq_j = 1.0 + 0.5 * np.cos(x[i+1])
            trig_coupling += np.sin(freq_i * x[i]) * np.cos(freq_j * x[i+1])
        result += 0.6 * trig_coupling
        
        # Adaptive polynomial distortions with dynamic exponents
        poly_distortion = 0.0
        for i in range(self.dim):
            exp_factor = 2.0 + 0.5 * np.sin(x[i])
            poly_distortion += 0.7 * x[i]**exp_factor
        result += poly_distortion
        
        # Novel hyperbolic sine-cosine interaction terms
        hyperbolic = 0.5 * np.sum(np.sinh(x) * np.cos(x) * np.tanh(x))
        
        # Multi-scale Gaussian peaks with varying widths
        gaussian_peaks = 0.0
        for i in range(self.dim):
            width = 0.5 + 0.3 * np.sin(x[i])
            gaussian_peaks += 0.9 * np.exp(-0.5 * (x[i] / width)**2) * np.cos(2.0 * x[i])**3
        result += gaussian_peaks
        
        # Saddle point perturbations with fractal-like behavior
        saddle = 0.4 * np.sum(np.sin(x**2) * np.cos(x) * np.sin(1.0 / (x**2 + 1e-6)))
        
        # Modified exponential coupling with logarithmic decay
        exp_coupling = 0.0
        for i in range(self.dim - 1):
            exp_coupling += np.exp(-0.3 * np.abs(x[i] - x[i+1])) * np.log(1.0 + 0.5 * (x[i] + x[i+1])**2)
        result += exp_coupling
        
        # Combine all terms
        result = result + hyperbolic + saddle + exp_coupling
        
        return result