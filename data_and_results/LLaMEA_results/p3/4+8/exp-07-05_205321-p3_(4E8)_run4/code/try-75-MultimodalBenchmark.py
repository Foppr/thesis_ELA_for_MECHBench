import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Base quadratic term with adaptive scaling
        quadratic = np.sum(x_norm**2) * 0.5
        
        # Chaotic sinusoidal component with time-delayed interactions
        chaotic = 0.0
        for i in range(self.dim):
            # Time-delayed sinusoidal with varying frequencies
            delayed = x_norm[i] + 0.3 * np.sin(3 * x_norm[(i-1) % self.dim]) if i > 0 else x_norm[i]
            chaotic += np.sin(2 * np.pi * delayed) * np.cos(1.5 * np.pi * delayed)
        
        # Adaptive frequency modulation based on distance from origin
        r = np.sqrt(np.sum(x_norm**2))
        freq_mod = 1.0 + 0.5 * np.sin(10 * r)
        
        # Multi-scale harmonic interactions
        harmonic = 0.0
        for i in range(self.dim):
            for k in range(1, 4):
                harmonic += (1.0 / k) * np.sin(k * freq_mod * np.pi * x_norm[i]) * np.cos(k * freq_mod * np.pi * x_norm[i])
        
        # Non-smooth component with clipped sinusoidal gradients
        smooth = 0.0
        for i in range(self.dim):
            smooth += np.abs(np.sin(5 * np.pi * x_norm[i])) * np.exp(-0.5 * r**2)
        
        # Cross-dimensional coupling with asymmetric interaction
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling += 0.2 * np.sin(3 * np.pi * x_norm[i]) * np.cos(2 * np.pi * x_norm[j]) * (1 + 0.1 * np.sin(4 * np.pi * r))
        
        # Add noise-like perturbations for increased complexity
        noise = 0.05 * np.sum(np.sin(7 * np.pi * x_norm) * np.cos(6 * np.pi * x_norm))
        
        # Combine all components with carefully tuned weights
        return 0.3 * quadratic + 0.4 * chaotic + 0.2 * harmonic + 0.05 * smooth + 0.05 * coupling + noise + 1.0