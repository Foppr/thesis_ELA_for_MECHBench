import numpy as np

class FractalSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-1, 1] range
        x_scaled = x / 5.0
        
        # Base quadratic term with adaptive conditioning
        quadratic = np.sum(x_scaled**2)
        
        # Fractal-like terrain with recursive harmonic modulation
        fractal_terrain = 0.0
        for i in range(self.dim):
            # Recursive harmonic components with varying frequencies and amplitudes
            freq = 2.0 + 3.0 * np.sin(x_scaled[i])
            amp = 1.0 + 0.5 * np.cos(4.0 * x_scaled[i])
            fractal_terrain += amp * np.sin(freq * x_scaled[i]) * np.cos(freq * x_scaled[i] * 2.0)
        
        # Dynamic saddle point structure with time-varying parameters
        saddle_structure = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Saddle point interaction with dynamic coupling strength
                coupling_strength = np.sin(2.0 * (x_scaled[i] + x_scaled[j])) * np.cos(3.0 * (x_scaled[i] - x_scaled[j]))
                dist = np.sqrt((x_scaled[i] - x_scaled[j])**2 + 0.01)
                saddle_structure += coupling_strength * np.exp(-dist**2) / (1.0 + dist**2)
        
        # Time-varying fitness landscape with multi-scale oscillations
        time_varying = 0.0
        for i in range(self.dim):
            # Multi-scale oscillation with varying periods and amplitudes
            period1 = 3.0 + 2.0 * np.sin(x_scaled[i])
            period2 = 5.0 + 3.0 * np.cos(x_scaled[i])
            time_varying += (np.sin(period1 * x_scaled[i]) * np.cos(period2 * x_scaled[i]) * 
                           np.exp(-x_scaled[i]**2 / 2.0))
        
        # Complex radial coupling with fractal dimensionality
        r = np.sqrt(np.sum(x_scaled**2))
        radial_coupling = 0.0
        for i in range(self.dim):
            # Fractal radial modulation
            radial_mod = np.sin(10.0 * x_scaled[i]) * np.cos(8.0 * x_scaled[i])
            radial_coupling += radial_mod * np.exp(-r**2 / 3.0)
        
        # Cross-dimensional coupling with adaptive weights and dynamic interactions
        cross_dim = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    # Adaptive coupling based on coordinate values
                    weight = 1.0 + 0.5 * np.sin(2.0 * x_scaled[i]) * np.cos(3.0 * x_scaled[j])
                    coupling = weight * np.sin(4.0 * (x_scaled[i] + x_scaled[j])) * np.cos(5.0 * (x_scaled[i] - x_scaled[j]))
                    cross_dim += coupling * np.exp(-0.5 * (x_scaled[i]**2 + x_scaled[j]**2))
        
        # Combine all components with dynamic weighting
        result = (quadratic + 0.8 * fractal_terrain + 0.9 * saddle_structure + 
                 0.7 * time_varying + 0.6 * radial_coupling + 0.5 * cross_dim)
        
        # Add adaptive noise based on position and dimensionality
        noise = 0.03 * np.random.normal(0.0, 1.0) * (1.0 + 0.4 * np.sin(25.0 * r))
        result += noise
        
        return result