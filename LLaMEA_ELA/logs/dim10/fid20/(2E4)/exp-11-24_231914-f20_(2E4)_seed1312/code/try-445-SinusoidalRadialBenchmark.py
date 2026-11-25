import numpy as np

class SinusoidalRadialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Sinusoidal components with varying frequencies and amplitudes
        self.sin_freq = np.random.uniform(1.0, 15.0, size=dim)
        self.sin_amp = np.random.uniform(0.5, 4.0, size=dim)
        # Radial basis function centers, widths, and weights
        self.rbf_centers = np.random.uniform(-4.0, 4.0, size=(dim, 4))
        self.rbf_widths = np.random.uniform(0.3, 2.5, size=(dim, 4))
        self.rbf_weights = np.random.uniform(-1.5, 1.5, size=(dim, 4))
        # Adaptive penalty parameters
        self.penalty_strength = np.random.uniform(1.5, 6.0, size=dim)
        self.penalty_exponent = np.random.uniform(2.5, 7.0, size=dim)
        # Dynamic scaling factors
        self.scale_factor = np.random.uniform(0.3, 2.5, size=dim)
        # Cross-dimensional coupling coefficients with stronger interactions
        self.coupling_coeffs = np.random.uniform(-1.0, 1.0, size=(dim, dim))
        # Phase shifts for sinusoidal components
        self.phase_shifts = np.random.uniform(0, 2*np.pi, size=dim)
        # Additional nonlinear term to increase complexity
        self.nonlinear_weights = np.random.uniform(-0.5, 0.5, size=dim)
        
    def f(self, x):
        # Scale input to [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Sinusoidal component
        sin_component = 0.0
        for i in range(self.dim):
            sin_val = self.sin_amp[i] * np.sin(self.sin_freq[i] * x[i] + self.phase_shifts[i])
            sin_component += sin_val
            
        # Radial basis function component
        rbf_component = 0.0
        for i in range(self.dim):
            rbf_val = 0.0
            for j in range(4):
                dist = np.sum((x - self.rbf_centers[i, j]) ** 2)
                rbf_val += self.rbf_weights[i, j] * np.exp(-dist / (2 * self.rbf_widths[i, j] ** 2))
            rbf_component += rbf_val
            
        # Adaptive penalty component
        penalty_component = 0.0
        for i in range(self.dim):
            dist_from_center = np.abs(x[i])
            penalty_val = self.penalty_strength[i] * (dist_from_center ** self.penalty_exponent[i])
            penalty_component += penalty_val
            
        # Dynamic scaling component
        scale_component = 0.0
        for i in range(self.dim):
            scale_val = self.scale_factor[i] * x[i]
            scale_component += scale_val
            
        # Cross-dimensional coupling component with quadratic interactions
        coupling_component = 0.0
        for i in range(self.dim):
            for j in range(self.dim):
                if i != j:
                    coupling_component += self.coupling_coeffs[i, j] * x[i] * x[j]
        
        # Additional nonlinear component
        nonlinear_component = 0.0
        for i in range(self.dim):
            nonlinear_component += self.nonlinear_weights[i] * (x[i] ** 3)
            
        # Combine all components with appropriate weights
        return (2.0 * sin_component + 
                1.5 * rbf_component + 
                1.2 * penalty_component + 
                1.0 * scale_component + 
                0.7 * coupling_component + 
                0.3 * nonlinear_component)