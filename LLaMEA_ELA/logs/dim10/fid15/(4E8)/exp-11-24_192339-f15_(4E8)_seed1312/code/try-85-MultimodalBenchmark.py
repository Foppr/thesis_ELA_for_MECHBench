import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Sphere function component
        sphere = np.sum(x**2)
        
        # Multimodal component with sine modulations and Gaussian decay
        multimodal = 0
        for i in range(self.dim):
            freq1 = 8 * (i + 1) / self.dim
            freq2 = 4.0 * (i + 1) / self.dim
            multimodal += np.sin(freq1 * np.pi * x[i]) ** 10 + 0.8 * np.exp(-0.5 * (x[i] / 1.2)**2) * np.cos(freq2 * np.pi * x[i]) ** 8
        
        # Enhanced polynomial interaction terms with higher-order cross-terms and quaternion-inspired coupling
        polynomial = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                polynomial += 0.15 * (x[i] ** 5) * (x[j] ** 7) * np.sin(np.pi * x[i] * x[j])
        
        # Adaptive scaling based on dimensionality with chaotic modulation
        scale_factor = 1.0 + 0.4 * np.log(self.dim + 1) + 0.05 * np.sin(2 * np.pi * self.dim / 3)
        
        # Global shift to increase landscape complexity with dynamic component
        shift = 1.1 * np.sum(np.abs(x)) + 0.1 * np.sum(np.sin(0.5 * np.pi * x))
        
        # Additional chaotic component for increased difficulty with quaternion-inspired terms
        chaotic = 0
        for i in range(self.dim):
            chaotic += 0.3 * np.sin(12 * np.pi * x[i] + np.cos(6 * np.pi * x[i])) ** 2 + 0.05 * np.sin(8 * np.pi * x[i]) * np.cos(4 * np.pi * x[i])
        
        # Quaternion-inspired cross-dimensional interaction
        quaternion_term = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                quaternion_term += 0.08 * (x[i]**2 + x[j]**2) * np.sin(np.pi * x[i] * x[j] / (self.dim + 1))
        
        # Combined function with improved fitness characteristics
        return sphere + scale_factor * (0.25 * multimodal + 0.08 * polynomial) + shift + chaotic + quaternion_term