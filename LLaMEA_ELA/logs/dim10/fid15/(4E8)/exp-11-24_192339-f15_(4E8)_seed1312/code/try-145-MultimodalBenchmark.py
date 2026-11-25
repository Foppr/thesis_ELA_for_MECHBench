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
            freq = 17 * (i + 1) / self.dim
            decay = np.exp(-0.3 * (x[i] / 1.5)**2)
            multimodal += decay * (np.sin(freq * x[i]) ** 17 + 0.8 * np.cos(freq * x[i]) ** 17)
        
        # Polynomial cross-dimensional interactions with varying exponents
        polynomial = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                exp_i = 6 + (i % 5)
                exp_j = 8 + (j % 4)
                polynomial += 0.25 * (x[i] ** exp_i) * (x[j] ** exp_j)
        
        # Dynamic radial basis function with logarithmic center spacing
        rbf = 0
        centers = np.logspace(-1, 1.2, min(7, self.dim))
        widths = np.linspace(0.6, 2.2, min(7, self.dim))
        for i in range(self.dim):
            center = centers[i % len(centers)]
            width = widths[i % len(widths)]
            rbf += 0.35 * np.exp(-0.5 * ((x[i] - center) / width)**2)
        
        # Quaternion-inspired coupling with hyperbolic tangent modulation
        quaternion = 0
        for i in range(0, self.dim, 2):
            if i + 1 < self.dim:
                term = np.tanh(x[i]) * np.tanh(x[i+1])
                quaternion += 0.45 * term * (x[i] - x[i+1])**2
        
        # Adaptive scaling factor with exponential dimensionality dependence
        scale_factor = 1.0 + 0.7 * np.log(self.dim + 1) + 0.2 * np.sqrt(self.dim)
        
        # Global shift component with cubic terms and linear combination
        shift = 1.3 * np.sum(x**3) + 0.9 * np.sum(np.abs(x))
        
        # Chaotic modulation with sine-cosine coupling
        chaotic = 0
        for i in range(self.dim):
            chaotic += 0.45 * np.sin(23 * x[i] + np.cos(11 * x[i])) * np.cos(17 * x[i] + np.sin(13 * x[i]))
        
        # Additional high-frequency oscillation component
        high_freq = 0
        for i in range(self.dim):
            high_freq += 0.35 * np.sin(37 * x[i]) * np.cos(29 * x[i])
        
        # Cross-dimensional coupling with exponential modulation
        cross_coupling = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_coupling += 0.3 * np.exp(-0.5 * (x[i] - x[j])**2) * np.sin(19 * (x[i] + x[j]))
        
        # Combined function with enhanced complexity and difficulty
        return sphere + scale_factor * (0.3 * multimodal + 0.2 * polynomial + 0.18 * rbf + 0.13 * quaternion + 0.07 * cross_coupling) + shift + chaotic + high_freq