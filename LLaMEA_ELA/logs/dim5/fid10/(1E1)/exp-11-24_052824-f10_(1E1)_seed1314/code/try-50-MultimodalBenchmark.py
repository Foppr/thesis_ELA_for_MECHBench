import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Sphere function component
        sphere = np.sum(x**2)
        
        # Enhanced multimodal component with improved chaotic interactions
        multimodal = 0
        for i in range(self.dim):
            # Increased complexity with higher frequency terms and better conditioning
            term1 = x[i]**2 - 10 * np.cos(2 * np.pi * x[i])
            term2 = 5 * np.sin(3 * np.pi * x[i])
            term3 = 3 * np.cos(5 * np.pi * x[i])
            term4 = 2 * np.sin(7 * np.pi * x[i])
            multimodal += term1 + term2 + term3 + term4
        
        # Improved exponential and polynomial interactions between dimensions
        interaction = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Enhanced coupling with more complex interaction terms
                interaction += np.exp(-0.1 * (x[i]**2 + x[j]**2)) * np.sin(0.5 * x[i] * x[j]) * np.cos(0.2 * (x[i] + x[j]))
        
        # Enhanced chaotic component with improved non-linearity
        chaotic = 0
        for i in range(self.dim):
            # Higher frequency oscillations and more complex combinations
            chaotic += np.sin(100 * x[i]) * np.cos(50 * x[i]) + np.log(1 + x[i]**2) + 0.1 * np.sin(200 * x[i])
        
        # Enhanced complexity component with better conditioning
        complexity = 0
        for i in range(self.dim):
            # More challenging polynomial with multiple roots and curvature changes
            complexity += (x[i]**4 - 6 * x[i]**2 + 8) * np.sin(x[i]) + 0.5 * x[i]**3
        
        # Enhanced high frequency component with better distribution
        high_freq = 0
        for i in range(self.dim):
            # More varied and complex high-frequency behavior
            high_freq += np.sin(20 * x[i]) * np.cos(15 * x[i]) + np.tanh(x[i])**3 + 0.3 * np.sin(50 * x[i])
        
        # Enhanced coupled component with more intricate dimension interactions
        coupled = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # More complex coupling with multiple interaction types
                coupled += (x[i]**2 + x[j]**2) * np.sin(0.1 * x[i] * x[j]) * np.cos(0.05 * x[i]**2 + x[j]**2) + 0.1 * np.exp(-x[i]**2 - x[j]**2)
        
        # Add a new component with enhanced non-convexity and challenging local minima
        non_convex = 0
        for i in range(self.dim):
            # Introduce more complex non-convex behavior
            non_convex += (x[i]**6 - 15 * x[i]**4 + 75 * x[i]**2 - 125) * np.cos(x[i]) + 0.2 * x[i]**5
        
        # Combine all components with optimized weights for better benchmark performance
        return sphere + 0.35 * multimodal + 0.25 * interaction + 0.45 * chaotic + 0.55 * complexity + 0.35 * high_freq + 0.25 * coupled + 0.3 * non_convex + 15 * np.sum(np.sin(x)**4)