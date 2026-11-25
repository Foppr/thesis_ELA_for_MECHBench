import numpy as np

class RotatingMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-5, 5] if not already
        x = np.clip(x, -5.0, 5.0)
        
        # Convert to polar coordinates for radial and angular components
        r = np.sqrt(np.sum(x**2))
        angles = np.arctan2(x[1], x[0]) if self.dim > 1 else 0.0
        
        # Radial harmonic component with multiple frequencies
        radial_harmonic = 0.0
        for i in range(1, 6):
            radial_harmonic += (1.0 / i) * np.sin(i * r) * np.cos(i * angles)
        
        # Angular periodic component with varying periods
        angular_periodic = 0.0
        for i in range(1, 8):
            angular_periodic += (0.5 / i) * np.cos(i * angles) * np.sin(i * r)
            
        # Rotating multimodal structure with adaptive conditioning
        rotating_modes = 0.0
        for i in range(self.dim):
            # Adaptive condition number based on dimension
            cond_num = 1.0 + 0.5 * np.sin(0.3 * i) * np.cos(0.2 * i**2)
            rotating_modes += cond_num * (np.sin(3.0 * x[i]) + 0.5 * np.cos(5.0 * x[i]))
            
        # Interference patterns from cross-dimensional interactions
        interference = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Phase-shifted interaction with distance-dependent strength
                dist = np.sqrt((x[i] - x[j])**2)
                phase_shift = np.sin(0.5 * (i + j))
                interference += 0.3 * phase_shift * np.cos(dist) * np.sin(2.0 * (x[i] + x[j]))
                
        # Multi-scale harmonic components with fractal-like behavior
        multi_scale = 0.0
        for i in range(self.dim):
            multi_scale += (0.4 * np.sin(2.0 * x[i]) * np.cos(3.0 * x[i]) + 
                           0.3 * np.cos(4.0 * x[i]) * np.sin(5.0 * x[i]) + 
                           0.2 * np.sin(6.0 * x[i]) * np.cos(7.0 * x[i]))
        
        # Adaptive conditioning with dimension-dependent scaling
        condition_scaling = 1.0
        for i in range(self.dim):
            condition_scaling += 0.1 * np.sin(0.5 * i) * np.cos(0.3 * i**2)
            
        # Penalty term for distance from origin to encourage convergence
        penalty = 0.1 * r**3
        
        # Combine all components with global scaling factor
        total = condition_scaling * (radial_harmonic + angular_periodic + rotating_modes + 
                                   interference + multi_scale) + penalty
        
        return total