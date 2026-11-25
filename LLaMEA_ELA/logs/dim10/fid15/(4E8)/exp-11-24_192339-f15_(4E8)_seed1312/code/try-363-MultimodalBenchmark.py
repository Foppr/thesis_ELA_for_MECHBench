import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Initialize fractal and oscillation parameters
        self.fractal_dim = 1.5 + 0.5 * np.random.rand()
        self.oscillation_freq = 2.0 + 1.0 * np.random.rand()
        self.ridge_strength = 0.8 + 0.4 * np.random.rand()
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Fractal-based oscillation component with adaptive scaling
        fractal_component = 0
        for i in range(self.dim):
            scale_factor = 1.0 + 0.3 * np.sin(0.5 * x[i] + self.dim * 0.2)
            fractal_component += scale_factor * np.sin(self.oscillation_freq * x[i]) * \
                               np.cos(self.oscillation_freq * x[i]**2) * \
                               np.exp(-0.1 * x[i]**2)
        
        # Dynamic ridge structure with variable curvature
        ridge_component = 0
        for i in range(self.dim):
            curvature = 1.0 + 0.5 * np.sin(0.3 * x[i] + self.dim * 0.1)
            ridge_component += curvature * (x[i]**3 - 3 * x[i]) * np.exp(-0.2 * x[i]**2)
        
        # Cross-dimensional interaction with time-varying coupling
        coupling_component = 0
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):
                coupling_strength = 0.7 + 0.3 * np.cos(0.4 * (x[i] + x[j]) + self.dim * 0.2)
                coupling_component += coupling_strength * np.sin(x[i] - x[j]) * \
                                   np.cos(x[i] + x[j]) * \
                                   np.exp(-0.1 * (x[i]**2 + x[j]**2))
        
        # Multi-frequency sinusoidal modulation with adaptive amplitude
        modulation_component = 0
        for i in range(self.dim):
            amp1 = 1.5 + 0.5 * np.sin(0.6 * x[i] + self.dim * 0.3)
            amp2 = 1.2 + 0.4 * np.cos(0.4 * x[i] + self.dim * 0.2)
            freq1 = 2.0 + 0.8 * np.sin(0.5 * x[i] + self.dim * 0.1)
            freq2 = 3.0 + 0.6 * np.cos(0.3 * x[i] + self.dim * 0.2)
            
            modulation_component += amp1 * np.sin(freq1 * x[i]) + \
                                  amp2 * np.cos(freq2 * x[i]**2) * \
                                  np.exp(-0.15 * x[i]**2)
        
        # Adaptive fractal interference pattern
        fractal_interference = 0
        for i in range(self.dim):
            fractal_scale = 2.0 + 0.8 * np.sin(0.7 * x[i] + self.dim * 0.3)
            fractal_interference += np.sin(fractal_scale * x[i]) * \
                                  np.cos(fractal_scale * x[i]**3) * \
                                  np.exp(-0.05 * x[i]**2)
        
        # Combine all components with dynamic weights
        return (0.3 * fractal_component + 0.25 * ridge_component + 
                0.2 * coupling_component + 0.15 * modulation_component + 
                0.1 * fractal_interference)