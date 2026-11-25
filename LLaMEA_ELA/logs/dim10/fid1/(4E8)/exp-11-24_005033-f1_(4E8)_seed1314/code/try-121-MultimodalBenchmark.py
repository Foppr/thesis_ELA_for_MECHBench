import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial potential components with varying degrees
        result = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Multi-degree polynomial with adaptive coefficients
            poly_term = (xi**2 + 0.5 * xi**3 + 0.1 * xi**4 + 0.05 * xi**5)
            result += poly_term
            
        # Radial basis function components with position-dependent widths
        rbf = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Adaptive width based on dimension and position
            width = 1.0 + 0.3 * np.abs(xi) + 0.2 * np.sin(0.5 * i)
            rbf += np.exp(-0.5 * (xi**2) / (width**2))
            
        # Quaternion-inspired rotational symmetries with directional bias
        rot_sym = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Rotational component with phase shift based on dimension
            phase = 0.2 * i * np.pi / self.dim if self.dim > 1 else 0
            rot_sym += np.sin(xi + phase) * np.cos(2 * xi + phase) * np.exp(-0.1 * xi**2)
            
        # Multi-scale harmonic oscillations with varying frequencies
        harmonic = 0.0
        for i in range(self.dim):
            xi = x[i]
            freq = 2.0 + 1.5 * np.sin(0.3 * i)
            amplitude = 1.0 + 0.5 * np.cos(0.4 * i)
            harmonic += amplitude * np.sin(freq * xi) * np.exp(-0.05 * xi**2)
            
        # Cross-dimensional coupling with directional dependency
        coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Directional coupling strength
                direction = np.sign(x[i] * x[j])
                coupling += 0.3 * direction * np.sin(x[i] + x[j]) * np.exp(-0.1 * (x[i]**2 + x[j]**2))
                
        # Asymmetric penalty with polynomial growth
        penalty = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Asymmetric penalty based on sign of variable
            if xi >= 0:
                penalty += 0.4 * xi**3
            else:
                penalty += 0.6 * np.abs(xi)**3.5
                
        # Combine all components with weighted contributions
        result = 0.8 * result + 0.3 * rbf + 0.5 * rot_sym + 0.4 * harmonic + 0.6 * coupling + penalty
        
        # Add global scaling and offset for improved fitness characteristics
        result = result * 1.2 + 0.5
        
        return result