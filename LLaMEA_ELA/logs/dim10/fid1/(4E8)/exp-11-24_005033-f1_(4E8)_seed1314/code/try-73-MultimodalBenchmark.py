import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base multimodal component with enhanced trigonometric interactions
        result = np.sum(np.log(1.0 + x**2 / 25.0)) + 2.5 * np.sum(np.cos(15 * x) * np.sin(20 * x)) + 0.03 * np.sum(x**4)
        
        # Enhanced polynomial conditioning with adaptive exponents
        result += 0.15 * np.sum((x**2 + x**3 + x**4) / (1.0 + np.abs(x)) * np.log(1.0 + np.abs(x)))
        
        # Introduce stronger cross-dimensional couplings with chaotic interactions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.04 * np.sin(12 * x[i]) * np.cos(12 * x[j]) * (x[i]**2 + x[j]**2) * np.exp(-0.15 * (x[i] - x[j])**2)
        
        # Add a chaotic component to increase landscape complexity
        chaos_term = 0.06 * np.sum(np.sin(27 * x) * np.cos(32 * x) * np.sin(38 * x))
        result += chaos_term
        
        # Add a novel coupling term with higher-order interactions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.015 * np.sin(6 * x[i]) * np.cos(6 * x[j]) * np.sin(8 * (x[i] + x[j])) * (x[i]**3 + x[j]**3)
        
        # Introduce a novel adaptive penalty based on gradient magnitude
        grad_magnitude = 0.0
        for i in range(self.dim):
            grad_magnitude += np.abs(np.cos(16 * x[i]) * np.sin(21 * x[i]))
        result += 0.12 * grad_magnitude**2
        
        return result