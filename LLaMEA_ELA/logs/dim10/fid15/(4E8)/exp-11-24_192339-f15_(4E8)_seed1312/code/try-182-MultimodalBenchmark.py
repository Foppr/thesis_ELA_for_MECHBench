import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic sine wave component with dynamic frequency modulation
        chaotic_wave = 0
        for i in range(self.dim):
            freq = 2.0 + 3.0 * np.sin(0.7 * i)
            chaotic_wave += np.sin(freq * x[i]) * np.cos(freq * x[i])
        
        # Radial basis functions with dynamic centers and widths
        rbf_sum = 0
        for i in range(self.dim):
            center = 3.0 * np.sin(0.5 * i)
            width = 1.0 + 0.5 * np.cos(0.3 * i)
            rbf_sum += np.exp(-0.5 * ((x[i] - center) / width)**2)
        
        # Polynomial interactions with asymmetric skewing
        poly_skew = 0
        for i in range(self.dim):
            skew_factor = 1.0 + 0.3 * np.sin(0.8 * i)
            poly_skew += (x[i]**3 + x[i]**5) * skew_factor
        
        # Cross-dimensional coupling with chaotic modulation
        cross_coupling = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = np.sin(0.5 * (i + j)) * np.cos(0.3 * (i - j))
                cross_coupling += coupling * x[i] * x[j]
        
        # Asymmetric exponential scaling
        exp_scaling = 0
        for i in range(self.dim):
            scale = 1.0 + 0.4 * np.sin(0.6 * i)
            exp_scaling += np.exp(scale * np.abs(x[i])) - 1.0
        
        # Dynamic conditioning based on dimensionality
        cond_factor = 1.0 + 0.2 * np.log(self.dim + 1)
        
        # Combine all components with appropriate weights
        return cond_factor * (0.3 * chaotic_wave + 0.25 * rbf_sum + 0.2 * poly_skew + 0.15 * cross_coupling) + exp_scaling