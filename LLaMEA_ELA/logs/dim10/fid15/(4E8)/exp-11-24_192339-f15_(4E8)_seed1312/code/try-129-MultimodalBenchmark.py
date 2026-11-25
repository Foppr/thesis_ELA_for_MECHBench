import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Sphere function component
        sphere = np.sum(x**2)
        
        # Exponential decay sinusoidal multimodal component with varying frequencies
        multimodal = 0
        for i in range(self.dim):
            freq = 13 * (i + 1) / self.dim
            decay = np.exp(-0.5 * (x[i] / 2.0)**2)
            multimodal += decay * (np.sin(freq * x[i]) ** 13 + 0.7 * np.cos(freq * x[i]) ** 13)
        
        # Polynomial cross-dimensional interactions with varying exponents
        polynomial = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                exp_i = 5 + (i % 4)
                exp_j = 7 + (j % 3)
                polynomial += 0.3 * (x[i] ** exp_i) * (x[j] ** exp_j)
        
        # Dynamic radial basis function with logarithmic center spacing
        rbf = 0
        centers = np.logspace(-1, 1, min(6, self.dim))
        widths = np.linspace(0.8, 2.0, min(6, self.dim))
        for i in range(self.dim):
            center = centers[i % len(centers)]
            width = widths[i % len(widths)]
            rbf += 0.4 * np.exp(-0.5 * ((x[i] - center) / width)**2)
        
        # Quaternion-inspired coupling with hyperbolic tangent modulation
        quaternion = 0
        for i in range(0, self.dim, 2):
            if i + 1 < self.dim:
                term = np.tanh(x[i]) * np.tanh(x[i+1])
                quaternion += 0.5 * term * (x[i] - x[i+1])**2
        
        # Adaptive scaling factor with exponential dimensionality dependence
        scale_factor = 1.0 + 0.6 * np.log(self.dim + 1) + 0.15 * np.sqrt(self.dim)
        
        # Global shift component with cubic terms and linear combination
        shift = 1.2 * np.sum(x**3) + 0.8 * np.sum(np.abs(x))
        
        # Chaotic modulation with sine-cosine coupling
        chaotic = 0
        for i in range(self.dim):
            chaotic += 0.5 * np.sin(19 * x[i] + np.cos(9 * x[i])) * np.cos(13 * x[i] + np.sin(7 * x[i]))
        
        # Additional high-frequency oscillation component
        high_freq = 0
        for i in range(self.dim):
            high_freq += 0.4 * np.sin(31 * x[i]) * np.cos(23 * x[i])
        
        # Combined function with enhanced complexity and difficulty
        return sphere + scale_factor * (0.35 * multimodal + 0.25 * polynomial + 0.2 * rbf + 0.15 * quaternion) + shift + chaotic + high_freq