import numpy as np

class ChaoticSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term with dynamic conditioning
        result = 0.1 * np.sum(x**2)
        
        # Chaotic saddle-point structures with time-varying parameters
        for i in range(self.dim):
            # Dynamic saddle point with chaotic modulation
            saddle_freq = 2.0 + 0.5 * np.sin(i * 0.7 + np.sum(x) * 0.3)
            saddle_amp = 1.5 + 0.8 * np.cos(i * 0.4 + np.sum(x) * 0.2)
            result += saddle_amp * np.sin(saddle_freq * x[i]) * np.cos(saddle_freq * x[i])
            
        # Fractal-quadratic hybrid interference patterns
        for i in range(self.dim):
            fractal_scale = 2.0 + 1.2 * np.sin(i * 0.6 + np.sum(x) * 0.4)
            result += 0.8 * (fractal_scale * x[i])**2 * np.sin(fractal_scale * x[i])
            
        # Multi-scale harmonic coupling with dynamic phase shifts
        for i in range(self.dim):
            phase_shift = 0.3 * np.sin(i * 0.5 + np.sum(x) * 0.2)
            freq = 1.5 + 0.7 * np.cos(i * 0.4 + np.sum(x) * 0.3)
            result += 1.2 * np.sin(freq * x[i] + phase_shift) * np.cos(freq * x[i] * 0.8 + phase_shift)
            
        # Dynamic dimensionality scaling with fractal interference
        dim_factor = 1.0 + 0.3 * np.sin(np.sum(x) * 0.5)
        for i in range(self.dim):
            result += 0.6 * dim_factor * np.exp(-0.5 * ((x[i] - 2.0 * np.sin(i * 0.3)) / 1.5)**2)
            
        # Chaotic harmonic ridge structures with varying amplitudes
        for i in range(self.dim):
            ridge_amp = 1.0 + 0.5 * np.cos(i * 0.8 + np.sum(x) * 0.4)
            ridge_freq = 3.0 + 2.0 * np.sin(i * 0.6)
            result += ridge_amp * np.sin(ridge_freq * x[i]) * np.cos(ridge_freq * x[i] * 0.7)
            
        # Asymmetric exponential barrier with chaotic modulation
        for i in range(self.dim):
            barrier_mod = 1.2 + 0.4 * np.sin(x[i] * 0.5 + np.sum(x) * 0.3)
            result += barrier_mod * np.exp(0.8 * abs(x[i]) / 5.0) * (1 + 0.3 * np.cos(x[i] * 2.0))
            
        # Saddle-point interaction terms between dimensions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                interaction = 0.5 * np.sin(0.5 * (x[i] + x[j]) + np.sum(x) * 0.2)
                result += interaction * np.exp(-0.5 * ((x[i] - x[j]) / 1.2)**2)
                
        # Multi-modal fractal basin structures
        r = np.sqrt(np.sum(x**2))
        if r > 0:
            basin_freq = 4.0 + 1.5 * np.sin(r * 0.2)
            result += 1.8 * np.sin(basin_freq * r) * np.cos(basin_freq * r * 0.4)
            
        return result