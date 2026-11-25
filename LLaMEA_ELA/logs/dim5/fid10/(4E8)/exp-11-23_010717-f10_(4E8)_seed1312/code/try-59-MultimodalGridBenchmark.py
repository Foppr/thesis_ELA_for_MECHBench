import numpy as np

class MultimodalGridBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-5, 5] if not already
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced fractal-like basin term with chaotic scaling
        basin = 0.15 * np.sum(x**2) + 0.05 * np.sum(np.sin(3.0 * x)**2)
        
        # Fractal-like grid of global minima terms with chaotic frequency modulation
        grid_minima = 0.0
        for i in range(self.dim):
            # Chaotic trigonometric pattern with varying frequencies and amplitudes
            freq1 = 1.5 + 0.5 * np.sin(i)
            freq2 = 2.0 + 0.3 * np.cos(i)
            grid_minima += 3.0 * np.sin(freq1 * x[i]) * np.cos(freq2 * x[i]) + \
                          1.2 * np.sin(freq2 * x[i]) * np.cos(freq1 * x[i]) + \
                          0.5 * np.sin(2.5 * x[i]) * np.cos(1.8 * x[i])
            
        # Enhanced cross-dimensional coupling with cubic and chaotic interactions
        cross_terms = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Chaotic cross-interactions with cubic and sinusoidal components
                cross_terms += 0.7 * np.sin(0.8 * x[i]) * np.cos(0.8 * x[j]) + \
                              0.35 * np.cos(1.2 * x[i]) * np.sin(1.2 * x[j]) + \
                              0.15 * (x[i]**3) * np.cos(0.6 * x[j]) + \
                              0.1 * (x[j]**3) * np.sin(0.5 * x[i]) + \
                              0.08 * np.sin(1.5 * x[i]) * np.sin(1.5 * x[j]) * np.cos(0.9 * x[i] + 0.7 * x[j])
        
        # Add chaotic noise term to increase challenge
        noise = 0.03 * np.sum(np.sin(6.0 * x) * np.cos(4.0 * x) * np.sin(2.0 * x))
        
        return basin + grid_minima + cross_terms + noise