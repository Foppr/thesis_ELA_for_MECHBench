import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] for stability
        x_scaled = x / 5.0
        
        # Polynomial chaos component with varying degrees and adaptive weights
        poly_chaos = np.sum((x_scaled**2 + 0.1 * x_scaled**4 + 0.01 * x_scaled**6) * 
                           (1.0 + 0.3 * np.sin(5 * x_scaled) * np.cos(3 * x_scaled)))
        
        # Trigonometric wave interference with frequency modulation and amplitude decay
        wave_interference = 0.0
        for i in range(self.dim):
            freq = 2**(i % 4 + 1)  # Varying frequencies with exponential spacing
            amp = 1.0 / (1.0 + 0.1 * i)
            wave_interference += amp * np.sin(freq * x_scaled[i]) * np.cos(freq * x_scaled[i])
        
        # Adaptive conditioning component with dimension-dependent difficulty
        conditioning = 0.0
        for i in range(self.dim):
            conditioning += (i + 1) * (x_scaled[i]**2 + 0.5 * x_scaled[i]**4)
        
        # Cross-dimensional interaction with asymmetric coupling
        cross_interaction = 0.0
        for i in range(self.dim - 1):
            cross_interaction += (i + 1) * np.sin(x_scaled[i] * x_scaled[i+1]) * \
                               np.exp(-0.5 * (x_scaled[i]**2 + x_scaled[i+1]**2))
        
        # Fractal-like oscillation with recursive frequency patterns
        fractal_osc = 0.0
        for i in range(min(4, self.dim)):
            base_freq = 3**(i + 1)
            fractal_osc += np.sin(base_freq * x_scaled[i % self.dim]) * \
                          np.cos(base_freq * x_scaled[(i+1) % self.dim]) * \
                          (0.5 + 0.5 * np.sin(2 * base_freq * x_scaled[i % self.dim]))
        
        # Asymmetric noise with multi-scale components
        noise = 0.01 * np.sum(np.sin(17 * x_scaled) * np.cos(13 * x_scaled) * 
                             (1.0 + 0.2 * np.sin(7 * x_scaled)))
        
        # Combine all components with carefully tuned weights
        return poly_chaos + 0.7 * wave_interference + 0.3 * conditioning + \
               0.4 * cross_interaction + 0.2 * fractal_osc + noise + 0.001 * np.sum(x_scaled**8)