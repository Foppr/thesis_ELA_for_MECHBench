import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute fractal-like patterns for memory-dependent evaluation
        self.fractal_patterns = np.random.uniform(-1, 1, (100, dim))
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Sphere function component
        sphere = np.sum(x**2)
        
        # Multimodal component with intensified chaotic sine modulations and Gaussian decay
        multimodal = 0
        for i in range(self.dim):
            freq1 = 40 * (i + 1) / self.dim
            freq2 = 20.0 * (i + 1) / self.dim
            multimodal += np.sin(freq1 * np.pi * x[i]) ** 35 + 0.95 * np.exp(-0.4 * (x[i] / 2.0)**2) * np.cos(freq2 * np.pi * x[i]) ** 35
        
        # Enhanced polynomial interaction terms with higher-order cross-terms and dynamic exponents
        polynomial = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                poly_exp = 2.5 + 0.8 * np.sin(0.7 * np.pi * (i + j))
                polynomial += 0.9 * (x[i] ** (10 + i % 4)) * (x[j] ** (15 + j % 5))
        
        # Quaternion-inspired cross-dimensional interactions with dynamic scaling and hyperbolic modulation
        quaternion = 0
        for i in range(0, self.dim, 2):
            if i + 1 < self.dim:
                quaternion += 1.2 * (x[i]**2 + x[i+1]**2) * np.tanh(np.pi * (x[i] - x[i+1])) * np.cos(0.95 * np.pi * (x[i] + x[i+1]))
        
        # Adaptive scaling based on dimensionality with exponential growth and logarithmic correction
        scale_factor = 2.5 + 2.0 * np.log(self.dim + 1) + 0.35 * np.sqrt(self.dim) + 0.1 * np.sin(0.45 * np.pi * self.dim)
        
        # Global shift to increase landscape complexity with enhanced nonlinearity
        shift = 3.5 * np.sum(np.abs(x)) + 0.6 * np.sum(x**5) + 0.2 * np.sum(np.sin(np.pi * x))
        
        # Additional chaotic component for increased difficulty with dynamic frequency and multiple harmonics
        chaotic = 0
        for i in range(self.dim):
            chaotic += 1.2 * np.sin(40 * np.pi * x[i] + np.cos(25 * np.pi * x[i]) + np.sin(10 * np.pi * x[i])) ** 7
        
        # Dynamic radial basis function component with varying centers, widths, and multiple Gaussian terms
        rbf = 0
        centers = np.linspace(-4.9, 4.9, min(20, self.dim))
        widths = np.linspace(1.0, 3.0, min(20, self.dim))
        for i in range(self.dim):
            center = centers[i % len(centers)]
            width = widths[i % len(widths)]
            rbf += 0.8 * np.exp(-0.5 * ((x[i] - center) / width)**2) + 0.4 * np.exp(-0.4 * ((x[i] - center) / (width * 1.4))**4)
        
        # Novel hyperbolic tangent-based cross-dimensional coupling with variable interaction strength
        coupling = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling += 0.6 * np.tanh(x[i]) * np.sin(np.pi * x[j]) * (x[i] - x[j])**6 + 0.2 * np.cos(np.pi * x[i]) * np.sinh(0.7 * x[j])
        
        # Additional sinusoidal modulation component with multiple frequencies and amplitude scaling
        modulated = 0
        for i in range(self.dim):
            modulated += 0.5 * np.sin(30 * np.pi * x[i] + 0.7 * np.cos(15 * np.pi * x[i])) ** 5
        
        # Fractal-like self-similarity component with memory-dependent evaluation
        fractal = 0
        for i in range(self.dim):
            pattern_idx = int(np.abs(x[i]) * 10) % len(self.fractal_patterns)
            pattern = self.fractal_patterns[pattern_idx]
            fractal += np.sum((x - pattern)**2) * 0.3
        
        # Memory-dependent fitness evaluation with delayed feedback
        memory_feedback = 0.05 * np.sum(np.sin(0.5 * np.pi * x)) * np.cos(0.3 * np.pi * np.sum(x))
        
        # Combined function with improved fitness characteristics and increased complexity
        return sphere + scale_factor * (0.55 * multimodal + 0.35 * polynomial + 0.4 * quaternion + 0.25 * coupling) + shift + chaotic + rbf + modulated + fractal + memory_feedback