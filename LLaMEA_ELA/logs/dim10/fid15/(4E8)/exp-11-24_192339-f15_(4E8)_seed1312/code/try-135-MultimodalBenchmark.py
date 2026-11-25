import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Sphere function component
        sphere = np.sum(x**2)
        
        # Multimodal component with intensified chaotic sine modulations and Gaussian decay
        multimodal = 0
        for i in range(self.dim):
            freq1 = 30 * (i + 1) / self.dim
            freq2 = 12.0 * (i + 1) / self.dim
            multimodal += np.sin(freq1 * np.pi * x[i]) ** 25 + 0.8 * np.exp(-0.3 * (x[i] / 1.5)**2) * np.cos(freq2 * np.pi * x[i]) ** 25
        
        # Enhanced polynomial interaction terms with higher-order cross-terms and dynamic exponents
        polynomial = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                poly_exp = 1.5 + 0.5 * np.sin(0.5 * np.pi * (i + j))
                polynomial += 0.7 * (x[i] ** (8 + i % 3)) * (x[j] ** (11 + j % 4))
        
        # Quaternion-inspired cross-dimensional interactions with dynamic scaling and hyperbolic modulation
        quaternion = 0
        for i in range(0, self.dim, 2):
            if i + 1 < self.dim:
                quaternion += 0.9 * (x[i]**2 + x[i+1]**2) * np.tanh(np.pi * (x[i] - x[i+1])) * np.cos(0.8 * np.pi * (x[i] + x[i+1]))
        
        # Adaptive scaling based on dimensionality with exponential growth and logarithmic correction
        scale_factor = 1.5 + 1.2 * np.log(self.dim + 1) + 0.2 * np.sqrt(self.dim) + 0.05 * np.sin(0.3 * np.pi * self.dim)
        
        # Global shift to increase landscape complexity with enhanced nonlinearity
        shift = 2.5 * np.sum(np.abs(x)) + 0.4 * np.sum(x**5) + 0.1 * np.sum(np.sin(np.pi * x))
        
        # Additional chaotic component for increased difficulty with dynamic frequency and multiple harmonics
        chaotic = 0
        for i in range(self.dim):
            chaotic += 0.8 * np.sin(30 * np.pi * x[i] + np.cos(15 * np.pi * x[i]) + np.sin(7 * np.pi * x[i])) ** 5
        
        # Dynamic radial basis function component with varying centers, widths, and multiple Gaussian terms
        rbf = 0
        centers = np.linspace(-4.9, 4.9, min(13, self.dim))
        widths = np.linspace(0.8, 2.2, min(13, self.dim))
        for i in range(self.dim):
            center = centers[i % len(centers)]
            width = widths[i % len(widths)]
            rbf += 0.6 * np.exp(-0.5 * ((x[i] - center) / width)**2) + 0.2 * np.exp(-0.3 * ((x[i] - center) / (width * 1.2))**3)
        
        # Novel hyperbolic tangent-based cross-dimensional coupling with variable interaction strength
        coupling = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling += 0.4 * np.tanh(x[i]) * np.sin(np.pi * x[j]) * (x[i] - x[j])**4 + 0.1 * np.cos(np.pi * x[i]) * np.sinh(0.5 * x[j])
        
        # Additional sinusoidal modulation component with multiple frequencies and amplitude scaling
        modulated = 0
        for i in range(self.dim):
            modulated += 0.3 * np.sin(20 * np.pi * x[i] + 0.5 * np.cos(10 * np.pi * x[i])) ** 3
        
        # Combined function with improved fitness characteristics and increased complexity
        return sphere + scale_factor * (0.45 * multimodal + 0.25 * polynomial + 0.3 * quaternion + 0.18 * coupling) + shift + chaotic + rbf + modulated