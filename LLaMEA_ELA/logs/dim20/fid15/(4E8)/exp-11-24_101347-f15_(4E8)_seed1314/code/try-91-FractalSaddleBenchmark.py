import numpy as np

class FractalSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Base quadratic term with dynamic conditioning
        base = np.sum(x_scaled**2)
        
        # Fractal-like component using recursive sine and cosine combinations
        fractal = 0.0
        for i in range(self.dim):
            val = x_scaled[i]
            for depth in range(1, 6):  # Recursive depth
                val = np.sin(2**depth * val) * np.cos(3**depth * val)
            fractal += val
        
        # Dynamic saddle point landscape with time-varying parameters
        saddle = 0.0
        for i in range(self.dim):
            # Time-varying parameters based on input coordinates
            a = 1.0 + 0.5 * np.sin(x_scaled[i] * 2.0)
            b = 1.0 + 0.3 * np.cos(x_scaled[i] * 3.0)
            c = 0.7 + 0.3 * np.sin(x_scaled[i] * 5.0)
            
            # Saddle point function with varying coefficients
            saddle += a * x_scaled[i]**2 - b * x_scaled[(i+1) % self.dim]**2 + c * x_scaled[i] * x_scaled[(i+1) % self.dim]
        
        # Multi-scale oscillatory component with adaptive frequencies
        oscillatory = 0.0
        for i in range(self.dim):
            freq = 2.0 + 3.0 * np.sin(x_scaled[i] * 0.5)
            amp = 1.5 + 0.5 * np.cos(x_scaled[i] * 1.5)
            oscillatory += amp * np.sin(freq * x_scaled[i]) * np.cos(freq * x_scaled[i])
        
        # Adaptive radial component with fractal scaling
        r = np.sqrt(np.sum(x_scaled**2))
        if r < 1e-8:
            radial = 0.0
        else:
            # Fractal-like radial scaling with multiple frequency components
            radial = 0.5 * (np.sin(10.0 * r) + np.cos(15.0 * r)) * np.exp(-r**2)
        
        # Dynamic coupling between dimensions with variable strength
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Variable coupling strength based on distance and input values
                dist = np.abs(x_scaled[i] - x_scaled[j])
                strength = 0.8 + 0.2 * np.sin(5.0 * (x_scaled[i] + x_scaled[j]))
                coupling += strength * np.sin(dist * 4.0) * np.cos(dist * 3.0)
        
        # Combine all components with adaptive weights that depend on input values
        weight_base = 1.0 + 0.1 * np.sin(r * 2.0)
        weight_fractal = 0.5 + 0.3 * np.cos(r * 1.5)
        weight_saddle = 0.8 + 0.2 * np.sin(r * 3.0)
        weight_oscillatory = 0.6 + 0.4 * np.cos(r * 2.5)
        
        result = (weight_base * base + 
                 weight_fractal * fractal + 
                 weight_saddle * saddle + 
                 weight_oscillatory * oscillatory + 
                 radial + 
                 coupling)
        
        # Add small noise for increased complexity
        result += 0.005 * np.random.uniform(-1.0, 1.0)
        
        return result