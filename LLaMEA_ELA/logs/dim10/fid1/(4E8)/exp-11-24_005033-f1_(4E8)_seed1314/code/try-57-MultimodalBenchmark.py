import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base multimodal component with enhanced trigonometric interactions
        result = np.sum(np.log(1.0 + x**2 / 25.0)) + 3.0 * np.sum(np.cos(15 * x) * np.sin(20 * x)) + 0.02 * np.sum(x**4)
        
        # Enhanced polynomial conditioning with adaptive exponents
        result += 0.2 * np.sum((x**2 + x**3 + x**4) / (1.0 + np.abs(x)) * np.log(1.0 + np.abs(x)))
        
        # Introduce stronger cross-dimensional couplings with chaotic interactions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.03 * np.sin(10 * x[i]) * np.cos(10 * x[j]) * (x[i]**2 + x[j]**2) * np.exp(-0.1 * (x[i] - x[j])**2)
        
        # Add a chaotic component to increase landscape complexity
        chaos_term = 0.05 * np.sum(np.sin(25 * x) * np.cos(30 * x) * np.sin(35 * x))
        result += chaos_term
        
        # Add a novel coupling term with higher-order interactions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.01 * np.sin(5 * x[i]) * np.cos(5 * x[j]) * np.sin(7 * (x[i] + x[j])) * (x[i]**3 + x[j]**3)
        
        # Introduce a novel adaptive penalty based on gradient magnitude
        grad_magnitude = 0.0
        for i in range(self.dim):
            grad_magnitude += np.abs(np.cos(15 * x[i]) * np.sin(20 * x[i]))
        result += 0.1 * grad_magnitude**2
        
        return result