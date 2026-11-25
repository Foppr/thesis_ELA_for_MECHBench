import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Sinusoidal oscillation component with varying frequencies and amplitudes
        sin_component = 0.0
        for i in range(self.dim):
            freq = 1.0 + 0.5 * np.sin(i * 0.7)
            amp = 1.0 + 0.3 * np.cos(i * 0.9)
            sin_component += amp * np.sin(freq * x[i]) * np.cos(freq * x[i] * 1.2)
        
        # Radial polynomial conditioning with adaptive exponents
        radial_poly = 0.0
        for i in range(self.dim):
            exp_factor = 1.5 + 0.5 * np.sin(i * 0.6)
            radial_poly += (x[i] ** exp_factor) * (1.0 + 0.2 * np.cos(i * 0.8))
        
        # Adaptive Gaussian peaks with dynamic positioning and scaling
        gaussian_sum = 0.0
        num_peaks = min(5, self.dim)
        for i in range(num_peaks):
            center = 3.0 * np.sin(i * np.pi / 2.0)
            width = 0.8 + 0.4 * np.cos(i * 0.5)
            height = 1.5 + 0.5 * np.sin(i * 0.7)
            gaussian_sum += height * np.exp(-0.5 * ((x[i] - center) / width)**2)
        
        # Coupled hyperbolic tangent terms with dynamic weights
        tanh_coupling = 0.0
        for i in range(self.dim - 1):
            weight = 0.6 + 0.4 * np.sin(i * 0.5)
            tanh_coupling += weight * np.tanh(x[i] + x[i+1]) * np.tanh(2.0 * x[i] - x[i+1])
        
        # Multi-scale chaotic modulation with dynamic frequency
        chaos_mod = 0.0
        for i in range(self.dim):
            freq_mod = 2.0 + 1.5 * np.sin(i * 0.3)
            chaos_mod += np.sin(freq_mod * x[i]) * np.cos(freq_mod * x[i] * 0.7) * \
                        (1.0 + 0.3 * np.sin(i * 0.9))
        
        # Combined function value with balanced contributions
        return 0.5 * sin_component + 0.3 * radial_poly + 0.4 * gaussian_sum + \
               0.6 * tanh_coupling + 0.2 * chaos_mod