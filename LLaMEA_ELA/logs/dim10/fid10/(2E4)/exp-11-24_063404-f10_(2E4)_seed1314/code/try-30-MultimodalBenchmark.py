import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-1, 1] for stability
        x_scaled = x / 5.0
        
        # Polynomial chaos component with varying degrees and random coefficients
        poly_chaos = np.sum((x_scaled**2 + 0.3 * x_scaled**4 + 0.1 * x_scaled**6) * 
                           np.random.uniform(0.5, 1.5, self.dim))
        
        # Trigonometric interference pattern with multiple frequencies and phase shifts
        trig_interference = np.sum(np.sin(12 * x_scaled + np.pi/4) * 
                                 np.cos(9 * x_scaled + np.pi/3) * 
                                 np.sin(7 * x_scaled + np.pi/6))
        
        # Asymmetric radial basis with clustered local minima
        r = np.sqrt(np.sum(x_scaled**2))
        radial_basis = np.sum(np.exp(-5 * (x_scaled - 0.3)**2) * 
                            np.sin(8 * np.arctan2(x_scaled[1], x_scaled[0]) if self.dim > 1 else 0))
        
        # Multi-scale oscillation with varying amplitudes and frequencies
        scale_osc = np.sum(np.sin(15 * x_scaled) * np.cos(13 * x_scaled) + 
                          0.5 * np.sin(25 * x_scaled) * np.cos(22 * x_scaled))
        
        # Cross-dimensional interaction with asymmetric coupling
        cross_interaction = 0.0
        if self.dim > 1:
            for i in range(self.dim - 1):
                cross_interaction += (x_scaled[i]**3 + x_scaled[i+1]**2) * np.sin(x_scaled[i] * x_scaled[i+1])
        
        # Add noise to increase ruggedness and non-smoothness
        noise = 0.005 * np.sum(np.random.normal(0, 1, self.dim))
        
        # Combine all components with weighted contributions
        return (0.4 * poly_chaos + 0.3 * trig_interference + 
                0.2 * radial_basis + 0.1 * scale_osc + 0.05 * cross_interaction + noise)