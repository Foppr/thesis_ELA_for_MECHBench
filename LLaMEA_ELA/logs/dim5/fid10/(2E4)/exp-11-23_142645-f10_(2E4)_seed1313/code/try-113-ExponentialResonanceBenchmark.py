import numpy as np

class ExponentialResonanceBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Exponential decay potentials with varying scales and centers
        potentials = 0.0
        for i in range(min(15, self.dim)):
            center = np.random.uniform(-4.5, 4.5)
            scale = np.random.uniform(0.5, 3.0)
            potentials += np.exp(-scale * np.abs(x - center))
        
        # Trigonometric resonance patterns with amplitude modulation
        resonance = 0.0
        for i in range(self.dim):
            amp = 1.0 + 0.5 * np.sin(0.5 * x[i])
            freq = 1.0 + 0.3 * np.cos(0.7 * x[i])
            resonance += amp * np.sin(freq * x[i]) * np.cos(0.8 * x[i])
        
        # Adaptive conditioning based on distance from origin
        condition = 0.0
        dist_from_origin = np.linalg.norm(x)
        if dist_from_origin < 2.0:
            condition = 0.5 * dist_from_origin**2
        else:
            condition = 0.3 * dist_from_origin**1.5 + 0.7 * dist_from_origin
        
        # Cross-term interactions with frequency-dependent coupling
        cross_terms = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                freq_coupling = 0.5 + 0.5 * np.sin(0.3 * (x[i] + x[j]))
                cross_terms += freq_coupling * np.exp(-0.5 * (x[i] - x[j])**2) * np.cos(2.0 * (x[i] + x[j]))
        
        # Asymmetric sigmoidal landscape with dynamic thresholds
        sigmoid_landscape = 0.0
        for i in range(self.dim):
            threshold = 0.5 * np.sin(0.4 * x[i])
            sigmoid_landscape += 1.0 / (1.0 + np.exp(-2.0 * (x[i] - threshold))) - 0.5
        
        # Add noise and scale components
        noise = 0.03 * np.random.rand()
        
        # Combine all components with adaptive weights based on position statistics
        mean_x = np.mean(np.abs(x))
        weight_potential = 0.3 + 0.2 * np.sin(0.5 * mean_x)
        weight_resonance = 0.25 + 0.15 * np.cos(0.3 * mean_x)
        weight_condition = 0.2 + 0.1 * np.sin(0.4 * mean_x)
        weight_cross = 0.15 + 0.1 * np.cos(0.6 * mean_x)
        weight_sigmoid = 0.1 + 0.05 * np.sin(0.7 * mean_x)
        
        total = (weight_potential * potentials + 
                weight_resonance * resonance + 
                weight_condition * condition + 
                weight_cross * cross_terms + 
                weight_sigmoid * sigmoid_landscape + 
                noise)
        
        return total