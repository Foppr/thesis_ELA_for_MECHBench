import numpy as np

class FractalMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.bounds = type('Bounds', (), {'lb': np.full(dim, -5.0), 'ub': np.full(dim, 5.0)})()
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Fractal component with self-similar structure using recursive sine waves
        fractal_term = 0.0
        for i in range(self.dim):
            # Recursive fractal pattern with diminishing amplitude
            amplitude = 1.0
            frequency = 3.0  # Changed from 2.0 to 3.0
            term = 0.0
            for depth in range(4):  # Increased recursion depth from 3 to 4
                term += amplitude * np.sin(frequency * x_norm[i])
                amplitude *= 0.4  # Changed from 0.5 to 0.4
                frequency *= 1.8  # Changed from 2.0 to 1.8
            fractal_term += term
        
        # Logarithmic conditioning that scales with dimensionality
        log_condition = 1.0 + 1.5 * np.log(1.0 + self.dim)  # Reduced coefficient from 2.0 to 1.5
        
        # Hybrid oscillatory terms with different frequencies and coupling
        hybrid_terms = 0.0
        for i in range(self.dim):
            # Primary oscillator with modified frequency
            primary = np.sin(3 * np.pi * x_norm[i])  # Changed from 2*pi to 3*pi
            # Coupled secondary oscillator
            if i > 0:
                coupled = np.cos(4 * np.pi * (x_norm[i] + x_norm[i-1]))  # Changed from 3*pi to 4*pi
            else:
                coupled = np.cos(4 * np.pi * x_norm[-1])  # Changed from 3*pi to 4*pi
            
            # Combined hybrid term with altered weighting
            hybrid_terms += primary * coupled
        
        # Multi-scale basin structure with varying curvature
        basin_term = 0.0
        for i in range(self.dim):
            # Different scaling factors for different dimensions
            scale_factor = 1.0 + 0.3 * np.sin(i * 1.5)  # Changed from 0.5 to 0.3 and added frequency factor
            basin_term += scale_factor * (x_norm[i]**2 + 0.4 * x_norm[i]**4)  # Changed 0.3 to 0.4
        
        # Cross-dimensional coupling with fractal-like interactions
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Fractal-like coupling with distance-dependent scaling
                dist = np.abs(x_norm[i] - x_norm[j])
                coupling = np.sin(7 * np.pi * dist) * np.exp(-dist**2)  # Changed frequency from 5*pi to 7*pi
                cross_term += coupling
        
        # Add noise component for increased complexity
        noise = 0.15 * np.random.rand()  # Increased noise level from 0.1 to 0.15
        
        # Combine all terms with proper weighting
        result = log_condition * (0.35 * fractal_term + 0.25 * hybrid_terms + 
                                0.25 * basin_term + 0.15 * cross_term) + noise
        
        return result