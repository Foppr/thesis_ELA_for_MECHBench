import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Sphere function component
        sphere = np.sum(x**2)
        
        # Highly multimodal component with enhanced chaotic interactions
        multimodal = 0
        for i in range(self.dim):
            # Enhanced trigonometric terms with higher frequencies and amplitudes
            term1 = x[i]**2 - 15 * np.cos(3 * np.pi * x[i]) + 5 * np.sin(4 * np.pi * x[i])
            term2 = 7 * np.cos(6 * np.pi * x[i]) - 3 * np.sin(7 * np.pi * x[i])
            multimodal += term1 + term2
        
        # Improved exponential and polynomial interactions between dimensions
        interaction = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # More complex interaction with combined exponential and polynomial terms
                interaction += np.exp(-0.05 * (x[i]**2 + x[j]**2)) * (x[i] * x[j])**2 + 0.1 * np.sin(2 * x[i] * x[j])
        
        # Enhanced chaotic component with more complex oscillations
        chaotic = 0
        for i in range(self.dim):
            # More intricate chaotic behavior with multiple frequency components
            chaotic += (np.sin(150 * x[i]) * np.cos(75 * x[i]) + np.tan(25 * x[i])) * np.log(1 + x[i]**2)
        
        # Enhanced complexity component with higher-order polynomials and sinusoidal modulation
        complexity = 0
        for i in range(self.dim):
            # Higher-order polynomial with sinusoidal modulation to increase non-linearity
            complexity += (x[i]**5 - 10 * x[i]**3 + 15 * x[i]) * np.cos(x[i])
        
        # Add a new highly oscillatory component to increase difficulty
        oscillatory = 0
        for i in range(self.dim):
            oscillatory += 20 * np.sin(20 * x[i]) * np.cos(10 * x[i]) + 5 * np.log(1 + np.abs(x[i]))
        
        # Combine all components with optimized weights to create a challenging landscape
        return sphere + 0.4 * multimodal + 0.3 * interaction + 0.5 * chaotic + 0.6 * complexity + 0.7 * oscillatory + 20 * np.sum(np.sin(x)**6)