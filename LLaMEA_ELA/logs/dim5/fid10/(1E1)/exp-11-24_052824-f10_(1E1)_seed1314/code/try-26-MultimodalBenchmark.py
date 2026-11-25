import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Sphere function component
        sphere = np.sum(x**2)
        
        # Highly multimodal component with chaotic interactions
        multimodal = 0
        for i in range(self.dim):
            # Multiple trigonometric terms with different frequencies and increased complexity
            term1 = x[i]**2 - 10 * np.cos(2 * np.pi * x[i])
            term2 = 5 * np.sin(3 * np.pi * x[i])
            term3 = 3 * np.cos(5 * np.pi * x[i])
            # Add higher frequency components for increased chaos
            term4 = 2 * np.sin(10 * np.pi * x[i])
            term5 = 1.5 * np.cos(7 * np.pi * x[i])
            multimodal += term1 + term2 + term3 + term4 + term5
        
        # Exponential and polynomial interactions between dimensions with stronger coupling
        interaction = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Increase the strength of interaction terms
                interaction += np.exp(-0.05 * (x[i]**2 + x[j]**2)) * np.sin(0.8 * x[i] * x[j]) * np.cos(0.3 * (x[i] + x[j]))
        
        # Add chaotic component with higher frequency oscillations and logarithmic scaling
        chaotic = 0
        for i in range(self.dim):
            # Introduce more complex chaotic behavior
            chaotic += (np.sin(150 * x[i]) * np.cos(75 * x[i]) + np.log(1 + x[i]**2)) * (1 + 0.1 * np.sin(20 * x[i]))
        
        # Add a new component that introduces more complex non-linearity and improves fitness
        complexity = 0
        for i in range(self.dim):
            # Increase polynomial degree and add coupling terms
            complexity += (x[i]**5 - 10 * x[i]**3 + 25 * x[i]) * np.sin(x[i]) + 0.5 * x[i]**4
        
        # Add a new component for enhanced multimodality with clustered local minima
        clustering = 0
        for i in range(self.dim):
            # Introduce sinusoidal modulation to create clustered valleys
            clustering += (np.sin(12 * x[i]) + np.cos(8 * x[i])) * np.exp(-0.5 * x[i]**2)
        
        # Combine all components with varying weights to create a challenging landscape
        return sphere + 0.4 * multimodal + 0.3 * interaction + 0.5 * chaotic + 0.6 * complexity + 0.7 * clustering + 20 * np.sum(np.sin(x)**5)