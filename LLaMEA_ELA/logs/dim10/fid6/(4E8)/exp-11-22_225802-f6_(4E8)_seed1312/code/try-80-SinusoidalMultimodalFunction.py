import numpy as np

class SinusoidalMultimodalFunction:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-3*pi, 3*pi] for increased sinusoidal complexity
        scaled_x = x * (3.0 * np.pi / 5.0)
        
        # Base chaotic sinusoidal component with multiple frequency interactions
        result = 0.0
        for i in range(self.dim):
            result += np.sin(scaled_x[i]) * np.cos(2.5 * scaled_x[i]) * np.sin(4 * scaled_x[i]) * np.cos(6 * scaled_x[i])
            
        # Add nested multi-scale quadratic valleys with dimensionally adaptive coefficients
        for i in range(self.dim):
            result += 0.4 * (np.sin(3 * scaled_x[i]) + 1) * (x[i]**2) * (1 + 0.3 * np.sin(7 * x[i]))
            
        # Introduce dynamic scaling with exponential weighting based on dimensionality
        dynamic_scale = np.sum(np.abs(x)) / self.dim
        exp_scale = np.exp(dynamic_scale)
        
        # Add ultra-high-frequency oscillations with variable amplitudes
        for i in range(self.dim):
            result += 0.5 * np.sin(23 * scaled_x[i]) * np.cos(17 * scaled_x[i]) * np.sin(11 * scaled_x[i])
            
        # Add global minimum penalty with non-linear scaling
        result += 0.2 * np.sum(x**2) + 0.1 * dynamic_scale**3 + 0.05 * exp_scale
        
        # Add complex cross-dimension interactions with varying coupling strengths
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = 0.1 * np.sin(2.2 * scaled_x[i]) * np.cos(3.7 * scaled_x[j])
                result += coupling * (1 + 0.2 * np.sin(x[i] + x[j]))
                
        # Add adaptive shift with chaotic modulation
        shift_term = 0.0
        for i in range(self.dim):
            shift_term += 0.1 * np.sin(0.8 * x[i]) * np.cos(1.3 * x[i])
        result += 0.12 * shift_term
        
        # Add a secondary landscape with fractal-like characteristics
        fractal_component = 0.0
        for i in range(self.dim):
            fractal_component += 0.08 * np.sin(5 * scaled_x[i]) * np.cos(9 * scaled_x[i]) * np.sin(13 * scaled_x[i])
        result += fractal_component * (1 + 0.15 * np.sin(np.sum(x)))
        
        return result