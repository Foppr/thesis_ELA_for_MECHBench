import numpy as np

class AdaptiveMultimodalLandscape:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Spherical component with adaptive scaling
        spherical = 0.5 * np.sum(x**2)
        
        # Step function component creating non-smooth regions
        step = np.sum(np.floor(0.5 + 0.5 * np.sin(3 * x)) * np.exp(-0.1 * x**2))
        
        # Sinusoidal oscillations with varying amplitudes and frequencies
        sinusoidal = np.sum(np.sin(2 * x) * np.cos(5 * x) * np.exp(-0.05 * x**2))
        
        # Multimodal component with multiple peaks and varying heights
        multimodal = 0.0
        for i in range(1, 6):
            center = np.full(self.dim, i * 0.8)
            multimodal += 2.0 * np.exp(-0.2 * np.sum((x - center)**2)) * np.sin(4 * np.pi * np.sum(x - center))
        
        # Asymmetric noise component to increase difficulty
        noise = 0.0
        for i in range(self.dim):
            noise += np.random.normal(0, 0.1) * np.exp(-0.02 * x[i]**2) * np.sin(10 * x[i])
        
        # Adaptive scaling based on coordinate values
        adaptive_scale = 1.0 + 0.3 * np.sum(np.abs(x) / 5.0)
        
        # Cross-dimensional interaction with asymmetric weights
        cross_interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                if i % 2 == 0:
                    cross_interaction += 0.5 * np.sin(x[i] * x[j]) * np.exp(-0.1 * (x[i]**2 + x[j]**2))
                else:
                    cross_interaction += 0.3 * np.cos(x[i] * x[j]) * np.exp(-0.08 * (x[i]**2 + x[j]**2))
        
        # Polynomial component with mixed degrees
        polynomial = 0.05 * np.sum(x**3) + 0.02 * np.sum(x**5)
        
        # Exponential decay with sinusoidal modulation
        exp_sin = 0.15 * np.sum(np.exp(-0.2 * x**2) * np.sin(8 * x))
        
        # Asymmetric step function with multiple thresholds
        asymmetric_step = 0.0
        for i in range(self.dim):
            if x[i] > 0:
                asymmetric_step += np.exp(-0.1 * x[i]) * np.sin(3 * x[i])
            else:
                asymmetric_step += np.exp(-0.05 * x[i]**2) * np.cos(2 * x[i])
        
        # Combined fitness value with adjusted weights
        return (spherical + 0.7 * step + 0.6 * sinusoidal + 0.8 * multimodal + 
                0.1 * noise + adaptive_scale + 0.4 * cross_interaction + 
                0.3 * polynomial + 0.25 * exp_sin + 0.35 * asymmetric_step)