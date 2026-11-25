import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced chaotic fractal structure with quantum-like interference
        fractal = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Multiple chaotic scales with varying frequencies and phases
            scales = [1.0, 0.7, 0.4, 0.2, 0.1]
            phases = [0.0, np.pi/4, np.pi/2, 3*np.pi/4, np.pi]
            for scale, phase in zip(scales, phases):
                fractal += np.sin(scale * xi**3 + phase) * np.cos(scale * xi**2 + phase) * np.exp(-scale * np.abs(xi))
        
        # Dynamic radial symmetry with quantum harmonic oscillation
        radial = 0.0
        centers = np.linspace(-4.8, 4.8, 13)
        for center in centers:
            dist = np.sum((x - center)**2)
            radial += np.exp(-0.03 * dist) * np.sin(6 * np.pi * dist**0.7) * np.cos(3 * np.pi * dist**0.5) * np.sin(2 * np.pi * dist**0.3)
        
        # Mixed high-order polynomial-trigonometric interactions with complex coupling
        poly_trig = 0.0
        for i in range(self.dim):
            poly_trig += (x[i]**7 - 4*x[i]**5 + 6*x[i]**3 - 4*x[i]) * np.sin(8*x[i]) * np.cos(8*x[i])
        
        # Exponentially decaying cross-term coupling with quantum interference
        cross = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.abs(x[i] - x[j])
                cross += np.exp(-dist**2) * np.sin(4*(x[i] + x[j])) * np.cos(6*(x[i] - x[j])) * np.sin(2 * np.pi * x[i] * x[j])
        
        # Boundary-adaptive penalty with hyperbolic scaling and quantum tunneling effect
        boundary = 0.0
        for i in range(self.dim):
            if np.abs(x[i]) > 4.6:
                boundary += np.log(1 + (np.abs(x[i]) - 4.6)**2) * (np.abs(x[i]) - 4.6)**4 * np.sin(5 * np.pi * (np.abs(x[i]) - 4.6))
        
        # Additional chaotic coupling terms with quantum phase modulation
        chaos = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                chaos += np.sin(2 * np.pi * x[i] * x[j]) * np.exp(-0.1 * (x[i]**2 + x[j]**2)) * np.cos(3 * np.pi * x[i] * x[j])
        
        # Quantum tunneling effect in high-dimensional space
        tunnel = 0.0
        for i in range(self.dim):
            tunnel += np.exp(-0.5 * x[i]**2) * np.sin(10 * x[i]) * np.cos(10 * x[i]) * np.sin(np.pi * x[i]**3)
        
        # Combined fitness function with enhanced dynamic weighting
        return 0.2 * fractal + 0.18 * radial + 0.22 * poly_trig + 0.17 * cross + 0.12 * boundary + 0.08 * chaos + 0.03 * tunnel