import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Spherical component with adaptive radius
        spherical = np.sum(x**2) * (1.0 + 0.1 * np.sin(self.dim))
        
        # Step function component with varying thresholds
        step = 0.0
        for i in range(self.dim):
            threshold = 2.0 * np.sin(i * 0.5)
            step += np.floor(np.abs(x[i]) - threshold) * np.cos(i)
        
        # Sinusoidal modulation with multi-frequency components
        sinusoidal = 0.0
        for i in range(self.dim):
            freq = 1.0 + 0.5 * np.sin(i * 0.3)
            sinusoidal += np.sin(freq * x[i]) * np.cos(freq * x[i]**2)
        
        # Cross-dimensional coupling with distance-based interaction
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.abs(x[i] - x[j])
                coupling += dist * np.exp(-dist**2) * np.sin(0.5 * (x[i] + x[j]))
        
        # Adaptive conditioning based on input magnitude and dimension
        condition = 1.0 + 0.2 * np.mean(np.abs(x)) + 0.1 * np.sin(self.dim * 0.4)
        
        # Multi-scale oscillation with varying amplitudes
        oscillation = 0.0
        for i in range(min(5, self.dim)):
            amp = 1.0 + 0.3 * np.cos(i * 0.7)
            freq = 2.0 + 0.5 * np.sin(i * 0.3)
            oscillation += amp * np.sin(freq * x[i])
        
        # Asymmetric penalty for large values
        penalty = 0.0
        for i in range(self.dim):
            if x[i] > 3.0:
                penalty += 0.5 * (x[i] - 3.0)**2
            elif x[i] < -3.0:
                penalty += 0.5 * (x[i] + 3.0)**2
        
        # Combine all components with noise
        result = condition * (spherical + step + sinusoidal) + coupling + oscillation + penalty
        
        # Add small random noise for robustness
        noise = 0.01 * np.random.rand()
        
        return result + noise