import numpy as np

class QuantumHarmonicBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Quantum harmonic oscillator parameters
        self.omega = 1.0
        self.hbar = 1.0
        self.mass = 1.0
        # Radial basis function parameters
        self.num_centers = min(20, dim * 2)
        self.rbf_width = 1.0
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Quantum harmonic oscillator component
        quantum_term = 0.0
        for i in range(self.dim):
            # Energy level contribution based on quantum harmonic oscillator
            n = int(np.abs(x[i]) / (self.hbar * self.omega / self.mass) + 0.5)
            energy = (n + 0.5) * self.hbar * self.omega
            quantum_term += energy * np.exp(-0.1 * x[i]**2)
            
        # Radial basis function interpolation component
        rbf_term = 0.0
        centers = np.random.uniform(-5.0, 5.0, (self.num_centers, self.dim))
        weights = np.random.normal(0, 1, self.num_centers)
        
        for i in range(self.num_centers):
            dist = np.linalg.norm(x - centers[i])
            rbf_val = weights[i] * np.exp(-0.5 * dist**2 / (self.rbf_width**2))
            rbf_term += rbf_val
            
        # Adaptive gradient clipping component
        grad_clip_term = 0.0
        for i in range(self.dim):
            # Compute gradient magnitude with adaptive clipping
            grad_magnitude = np.abs(x[i]) * (1.0 + 0.1 * np.sin(0.3 * x[i]))
            clip_factor = 1.0 / (1.0 + np.exp(-grad_magnitude))
            grad_clip_term += clip_factor * np.cos(0.4 * x[i])**2
            
        # Multi-dimensional coupling with quantum phase shifts
        coupling_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Phase-shifted interaction
                phase_shift = np.sin(0.5 * (x[i] + x[j]))
                coupling_val = (x[i]**2 + x[j]**2) * np.cos(x[i] - x[j] + phase_shift)
                coupling_term += coupling_val
                
        # Boundary conditioning with quantum-like tunneling effect
        boundary_term = 0.0
        for i in range(self.dim):
            if np.abs(x[i]) > 4.5:
                dist_from_boundary = 5.0 - np.abs(x[i])
                tunnel_prob = np.exp(-dist_from_boundary**2)
                boundary_term += tunnel_prob * np.sin(2.0 * x[i])**2
                
        # Global scaling with time-varying quantum parameter
        r = np.sqrt(np.sum(x**2))
        global_scale = 1.0 + 0.2 * np.cos(0.3 * r)
        
        # Combine all terms
        total = quantum_term + rbf_term + grad_clip_term + coupling_term + boundary_term
        return total * global_scale