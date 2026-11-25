import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Base quadratic term with dynamic conditioning
        base = np.sum(x_scaled**2)
        
        # Enhanced fractal-like component using nested trigonometric functions
        fractal = 0.0
        for i in range(self.dim):
            val = x_scaled[i]
            # Deep recursive trigonometric nesting
            for depth in range(1, 8):  
                val = np.sin(2**depth * val) * np.cos(3**depth * val) + 0.1 * np.sin(5**depth * val)
            fractal += val
        
        # Dynamic saddle point landscape with complex coupling
        saddle = 0.0
        for i in range(self.dim):
            # Complex time-varying parameters based on input coordinates
            a = 1.0 + 0.8 * np.sin(x_scaled[i] * 2.0 + np.cos(x_scaled[i]))
            b = 1.0 + 0.6 * np.cos(x_scaled[i] * 3.0 + np.sin(x_scaled[i]))
            c = 0.7 + 0.5 * np.sin(x_scaled[i] * 5.0 + np.cos(x_scaled[i] * 2.0))
            
            # Enhanced saddle point function with cubic terms
            saddle += a * x_scaled[i]**2 - b * x_scaled[(i+1) % self.dim]**2 + c * x_scaled[i] * x_scaled[(i+1) % self.dim] + 0.3 * x_scaled[i]**3
        
        # Multi-scale oscillatory component with adaptive frequencies and amplitudes
        oscillatory = 0.0
        for i in range(self.dim):
            freq = 2.0 + 4.0 * np.sin(x_scaled[i] * 0.5 + 0.5 * np.cos(x_scaled[i]))
            amp = 1.5 + 0.8 * np.cos(x_scaled[i] * 1.5 + 0.3 * np.sin(x_scaled[i]))
            # Add complex phase modulation
            phase = 0.2 * np.sin(3.0 * x_scaled[i])
            oscillatory += amp * np.sin(freq * x_scaled[i] + phase) * np.cos(freq * x_scaled[i] + phase)
        
        # Enhanced radial component with multiple fractal scales and decay
        r = np.sqrt(np.sum(x_scaled**2))
        if r < 1e-8:
            radial = 0.0
        else:
            # Multi-fractal radial scaling with varying decay rates
            radial = (np.sin(15.0 * r) + np.cos(20.0 * r)) * np.exp(-r**3) + 0.5 * (np.sin(8.0 * r) + np.cos(12.0 * r)) * np.exp(-r**2)
        
        # Advanced coupling between dimensions with non-linear strength
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Non-linear coupling strength based on distance and input values
                dist = np.abs(x_scaled[i] - x_scaled[j])
                strength = 0.8 + 0.4 * np.sin(5.0 * (x_scaled[i] + x_scaled[j]) + 0.3 * np.cos(x_scaled[i] * x_scaled[j]))
                # Add higher-order interaction terms
                coupling += strength * (np.sin(dist * 4.0) * np.cos(dist * 3.0) + 0.2 * np.sin(dist * 7.0))
        
        # Combine all components with enhanced adaptive weights
        weight_base = 1.0 + 0.2 * np.sin(r * 3.0)
        weight_fractal = 0.6 + 0.4 * np.cos(r * 2.0)
        weight_saddle = 0.9 + 0.3 * np.sin(r * 4.0)
        weight_oscillatory = 0.7 + 0.5 * np.cos(r * 3.5)
        
        result = (weight_base * base + 
                 weight_fractal * fractal + 
                 weight_saddle * saddle + 
                 weight_oscillatory * oscillatory + 
                 radial + 
                 coupling)
        
        # Add enhanced noise for increased complexity and robustness
        noise_amplitude = 0.01 * (1.0 + 0.5 * np.sin(r * 2.0))
        result += noise_amplitude * np.random.uniform(-1.0, 1.0)
        
        return result