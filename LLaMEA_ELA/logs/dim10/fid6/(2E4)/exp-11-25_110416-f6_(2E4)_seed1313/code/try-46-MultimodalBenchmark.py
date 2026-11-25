import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        result = np.sum(x**2)
        
        # Add exponentially decaying sinusoidal components with varying frequencies and amplitudes
        for i in range(self.dim):
            freq = 3 ** (i % 6 + 1)
            decay = np.exp(-0.15 * np.abs(x[i]))
            amplitude = 0.8 + 0.2 * np.sin(0.5 * i)
            result += decay * amplitude * np.sin(freq * x[i]) * np.cos(freq * x[i] * 0.4)
            
        # Add adaptive polynomial penalties with altered exponents and coefficients
        for i in range(self.dim):
            power = 3 + (i % 5) + 0.5 * np.sin(i * 0.7)
            result += 0.3 * (x[i] - 1.5)**power + 0.25 * (x[i] + 1.8)**(power + 1)
            
        # Add a complex global minimum structure with multiple peaks and varying scales
        for i in range(self.dim):
            result += 0.1 * np.exp(-0.5 * ((x[i] - 1.5) / 0.4)**2) * np.sin(30 * x[i])
            
        # Add cross-dimensional coupling with stronger interaction strength and wider range
        for i in range(self.dim):
            for j in range(i+1, min(i+8, self.dim)):
                interaction = (x[i]**2 + x[j]**2) * np.cos(0.5 * (x[i] - x[j]))
                result += 0.06 * interaction
                
        # Add a more chaotic component with nested sinusoidal patterns and different scaling
        chaotic_term = 0.07 * np.sum(np.sin(20 * x) * np.cos(10 * x) * np.sin(5 * x))
        result += chaotic_term
        
        # Add asymmetric basin components to increase conditioning difficulty
        asymmetry = 0.03 * np.sum(np.abs(x) ** 1.7 * np.sign(x))
        result += asymmetry
        
        # Introduce modified chaotic component with nested sinusoidal patterns and altered scaling
        nested_chaos = 0.05 * np.sum(np.sin(25 * x) * np.cos(15 * x) * np.sin(8 * x) * np.cos(4 * x))
        result += nested_chaos
        
        # Adjust polynomial penalties with dynamic exponents
        for i in range(self.dim):
            dynamic_power = 3 + (i % 4) + 0.3 * np.cos(i * 0.5)
            result += 0.2 * (x[i] - 1.2)**dynamic_power + 0.3 * (x[i] + 1.5)**(dynamic_power + 1.5)
            
        return result