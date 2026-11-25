import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Sphere function component
        sphere = np.sum(x**2)
        
        # Multimodal component with chaotic logistic modulations and Gaussian decay
        multimodal = 0
        for i in range(self.dim):
            r = 3.95 + 0.05 * np.sin(0.7 * np.pi * i)
            logistic = r * x[i] * (1 - x[i])
            multimodal += np.sin(20 * np.pi * logistic) ** 20 + 0.8 * np.exp(-0.3 * (x[i] / 2.0)**2) * np.cos(10 * np.pi * x[i]) ** 20
        
        # Elliptic component with dynamic scaling and varying exponents
        elliptic = 0
        for i in range(self.dim):
            exponent = 2.0 + 1.5 * np.sin(0.5 * np.pi * i)
            elliptic += (x[i] ** exponent) * (1.0 + 0.1 * np.cos(3 * np.pi * x[i]))
        
        # Quaternion-inspired cross-dimensional interactions with secant scaling
        quaternion = 0
        for i in range(0, self.dim, 2):
            if i + 1 < self.dim:
                secant_term = 1.0 / np.cosh(x[i] - x[i+1])
                quaternion += 0.9 * (x[i]**2 + x[i+1]**2) * secant_term * np.sin(0.8 * np.pi * (x[i] + x[i+1]))
        
        # Dynamic scaling factor based on dimensionality with exponential growth
        scale_factor = 1.5 + 2.0 * np.log(self.dim + 1) + 0.4 * np.sqrt(self.dim) + 0.1 * np.cos(0.3 * np.pi * self.dim)
        
        # Global shift to increase landscape complexity with enhanced nonlinearity
        shift = 2.5 * np.sum(np.abs(x)) + 0.4 * np.sum(x**4) + 0.2 * np.sum(np.tan(x))
        
        # Additional chaotic component with multiple logistic mappings and harmonics
        chaotic = 0
        for i in range(self.dim):
            chaotic += 1.2 * np.sin(30 * np.pi * x[i] + np.cos(15 * np.pi * x[i]) + np.sin(5 * np.pi * x[i])) ** 5
        
        # Dynamic radial basis function component with varying centers and widths
        rbf = 0
        centers = np.linspace(-4.5, 4.5, min(20, self.dim))
        widths = np.linspace(1.0, 3.0, min(20, self.dim))
        for i in range(self.dim):
            center = centers[i % len(centers)]
            width = widths[i % len(widths)]
            rbf += 0.6 * np.exp(-0.5 * ((x[i] - center) / width)**2) + 0.4 * np.exp(-0.3 * ((x[i] - center) / (width * 1.5))**3)
        
        # Novel hyperbolic secant-based cross-dimensional coupling with variable interaction strength
        coupling = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling += 0.4 * np.sech(x[i]) * np.sin(np.pi * x[j]) * (x[i] - x[j])**4 + 0.2 * np.cos(np.pi * x[i]) * np.tanh(0.7 * x[j])
        
        # Additional sinusoidal modulation component with multiple frequencies and amplitude scaling
        modulated = 0
        for i in range(self.dim):
            modulated += 0.5 * np.sin(30 * np.pi * x[i] + 0.7 * np.cos(15 * np.pi * x[i])) ** 3
        
        # Combined function with improved fitness characteristics and increased complexity
        return sphere + scale_factor * (0.4 * multimodal + 0.25 * elliptic + 0.3 * quaternion + 0.2 * coupling) + shift + chaotic + rbf + modulated