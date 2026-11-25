import numpy as np

class SinusoidalQuadraticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        x = np.array(x)
        
        # Sinusoidal oscillations with varying frequencies and amplitudes
        sinusoidal = np.sum(np.sin(2 * np.pi * x) * np.cos(3 * np.pi * x) * 
                           (1 + 0.5 * np.sin(0.5 * x**2)))
        
        # Polynomial penalty terms with multiple local minima
        polynomial = np.sum(x**4 - 8 * x**2 + 16)
        
        # Cross-dimensional quadratic interactions with varying coupling strengths
        quadratic_interactions = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                quadratic_interactions += 0.5 * (x[i]**2 + x[j]**2) * \
                                       np.exp(-0.1 * (x[i] - x[j])**2) * \
                                       np.sin(2 * np.pi * (x[i] + x[j]))
                
        # Additional multimodal component with Gaussian-like peaks
        gaussian_peaks = 0
        for i in range(self.dim):
            gaussian_peaks += np.exp(-0.5 * (x[i] - 2)**2) * \
                            np.exp(-0.5 * (x[i] + 2)**2) * \
                            np.sin(4 * x[i])
        
        # Combine all components with appropriate weights
        return 1.2 * sinusoidal + 0.8 * polynomial + 0.6 * quadratic_interactions + 0.4 * gaussian_peaks