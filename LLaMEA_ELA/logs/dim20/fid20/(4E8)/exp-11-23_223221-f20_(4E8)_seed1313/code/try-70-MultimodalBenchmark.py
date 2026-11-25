import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        result = 0.0
        
        # Enhanced chaotic sine oscillations with dynamic frequencies and phase shifts
        for i in range(self.dim):
            freq = 2.0 + 0.8 * np.sin(i * np.pi / 2.5) + 0.4 * np.cos(i * np.pi / 3.0) + 0.2 * np.sin(i * np.pi / 1.7)
            phase = 0.5 * np.sin(i * np.pi / 4.0) + 0.3 * np.cos(i * np.pi / 2.3)
            result += (np.sin(freq * x[i] + phase) * np.cos(freq * x[i]**2 + phase) + 
                      0.2 * np.sin(8 * x[i] + phase) + 0.1 * np.sin(12 * x[i] + phase))
        
        # Higher-order polynomial interaction terms with cross-dimension coupling and adaptive exponents
        for i in range(self.dim):
            for j in range(i+1, min(i+5, self.dim)):  # Increased cross-dimension interaction
                exp_i = 3.0 + 0.5 * np.sin(i * np.pi / 3.0)
                exp_j = 2.5 + 0.4 * np.cos(j * np.pi / 2.5)
                result += 0.12 * (x[i]**exp_i) * (x[j]**exp_j) * np.exp(-0.2 * (x[i]**2 + x[j]**2))
        
        # Multi-scale exponential decay with trigonometric modulation and adaptive amplitudes
        decay_term = 0.0
        for i in range(self.dim):
            amp1 = 0.6 + 0.2 * np.sin(i * np.pi / 3.0)
            amp2 = 0.4 + 0.1 * np.cos(i * np.pi / 2.0)
            decay_term += (amp1 * np.exp(-0.4 * x[i]**2) * np.cos(4 * np.pi * x[i]) + 
                          amp2 * np.exp(-0.8 * x[i]**2) * np.sin(5 * np.pi * x[i]))
        result += 0.5 * decay_term
        
        # Noise-like perturbations with varying amplitudes and chaotic modulation
        noise = 0.0
        for i in range(self.dim):
            amp = 0.05 + 0.02 * np.sin(i * np.pi / 2.0)
            noise += amp * (np.sin(13 * x[i]) * np.cos(10 * x[i]) + 
                           0.8 * np.sin(16 * x[i]) + 0.6 * np.sin(19 * x[i]))
        result += noise
        
        # Add a global scaling factor with chaotic modulation to control landscape difficulty
        global_scale = 1.0 + 0.2 * np.sin(np.sum(x**3) / self.dim)
        result *= global_scale
        
        # Add a complex multi-modal component with multiple local minima
        multimodal = 0.0
        for i in range(self.dim):
            multimodal += (0.3 * np.sin(6 * x[i]) * np.cos(9 * x[i]) + 
                          0.2 * np.sin(10 * x[i]) * np.cos(7 * x[i]))
        result += 0.3 * multimodal
        
        # Normalize and return
        return result / self.dim