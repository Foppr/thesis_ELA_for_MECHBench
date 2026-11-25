import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Fractal-like chaotic component with memory effects
        fractal_component = 0.0
        for i in range(self.dim):
            # Memory-dependent chaotic modulation
            if i > 0:
                mem_factor = 0.5 + 0.5 * np.sin(0.3 * x[i-1])
            else:
                mem_factor = 1.0
            
            freq = 3.0 + 2.0 * np.sin(0.4 * x[i]) * np.cos(0.5 * x[i]) * mem_factor
            amp = 1.5 + 1.0 * np.sin(0.6 * x[i])
            fractal_component += amp * np.sin(freq * x[i] + 0.3 * np.sin(4.0 * x[i]) + 0.1 * np.sin(7.0 * x[i]))
        
        # Memory-dependent Gaussian peaks with dynamic parameters
        gaussian_peaks = 0.0
        for i in range(self.dim):
            # Peak positions and heights depend on previous evaluations
            peak_pos = (i % 3) + 0.5 * np.sin(0.2 * x[i])
            peak_height = 3.0 + 2.0 * np.cos(0.7 * x[i])
            peak_width = 0.4 + 0.3 * np.sin(0.3 * x[i])
            
            gaussian_peaks += peak_height * np.exp(-0.5 * ((x[i] - peak_pos) / peak_width)**2)
        
        # Cross-dimensional asymmetric polynomial coupling with chaotic interaction
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):
                # Chaotic interaction strength
                strength = 1.5 + 1.0 * np.sin(0.3 * (x[i] + x[j]))
                # Asymmetric coupling term
                asym_factor = 1.0 + 0.5 * np.cos(0.4 * x[i]) * np.sin(0.2 * x[j])
                coupling += strength * asym_factor * (x[i]**3 + x[j]**3) * np.sin(0.8 * (x[i] - x[j]))
        
        # Dynamic elliptic valley with fractal scaling
        valley = 0.0
        for i in range(self.dim):
            # Fractal-like scaling parameters
            scale_a = 1.0 + 0.3 * np.cos(0.2 * x[i])
            scale_b = 0.8 + 0.4 * np.sin(0.15 * x[i])
            scale_c = 1.2 + 0.6 * np.tan(0.05 * x[i])
            
            # Fractal-like valley shape
            valley += ((x[i] - scale_a * np.sin(0.3 * x[i]))**2 / scale_a + 
                      (x[i] - scale_b * np.cos(0.2 * x[i]))**2 / scale_b + 
                      (x[i] - scale_c * np.exp(-0.05 * x[i]))**2 / scale_c)
        
        # Multi-scale saddle-point structure with memory effects
        saddle = 0.0
        for i in range(self.dim):
            if i < self.dim - 1:
                # Memory-dependent modulations
                mod1 = 0.8 + 0.4 * np.sin(0.6 * x[i]) * np.cos(0.3 * x[i-1] if i > 0 else 0)
                mod2 = 0.7 + 0.3 * np.cos(0.4 * x[i+1])
                saddle += (x[i]**2 - x[i+1]**2) * mod1 + (x[i+1]**2 - x[i]**2) * mod2
        
        # High-frequency oscillatory component with chaotic decay
        high_freq = 0.0
        for i in range(self.dim):
            # Chaotic amplitude modulation
            amp = 1.2 + 0.8 * np.sin(1.5 * x[i]) * np.cos(0.7 * x[i-1] if i > 0 else 0)
            high_freq += amp * np.sin(20.0 * x[i]) * np.exp(-0.3 * x[i]**2)
        
        # Dimensionally varying normalization factor with fractal scaling
        norm_factor = 1.5 + 0.3 * np.log(self.dim + 1) + 0.1 * np.sin(0.1 * self.dim)
        
        return (0.20 * fractal_component + 0.25 * gaussian_peaks + 
                0.20 * coupling + 0.15 * valley + 0.10 * saddle + 0.10 * high_freq) * norm_factor