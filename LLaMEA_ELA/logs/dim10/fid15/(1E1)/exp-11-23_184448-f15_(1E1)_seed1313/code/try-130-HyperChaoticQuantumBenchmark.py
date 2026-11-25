import numpy as np

class HyperChaoticQuantumBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        x = np.array(x)
        
        # Quantum superposition radial term with phase interference
        r_squared = np.sum(x**2)
        quantum_radial = np.exp(-0.15 * r_squared) * np.sin(r_squared * 0.5 + np.pi/4) * (r_squared + 1e-8)
        
        # Hyper-chaotic saddle points with quantum tunneling effects
        hyper_saddle = 0.0
        for i in range(self.dim):
            # Quantum coupling with delayed interaction
            delay_idx = (i + self.dim//2) % self.dim
            freq = 4.0 + 3.0 * np.sin(i * np.pi / (self.dim + 2))
            tunneling = np.exp(-0.5 * (x[i] - x[delay_idx])**2)
            hyper_saddle += np.cos(x[i] * freq) * np.sin(x[i] * freq) * tunneling
        
        # Temporal coupling with adaptive fractal scaling
        temporal_coupling = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.sqrt((x[i] - x[j])**2 + 1e-8)
                # Adaptive fractal dimension scaling
                fractal_dim = 1.5 + 0.5 * np.sin(np.log(dist + 1) * 2)
                temporal_coupling += (x[i]**4 + x[j]**4) * np.exp(-0.3 * dist) * (dist ** (-fractal_dim))
        
        # Multi-scale quantum basin landscape with adaptive depths
        quantum_basins = 0.0
        for i in range(self.dim):
            center = 2.5 * np.sin(i * np.pi / (self.dim + 4)) * np.cos(i * np.pi / (self.dim + 6))
            depth = 1.5 + 0.8 * np.sin(i * np.pi / (self.dim + 3))
            # Quantum probability amplitude
            amplitude = np.exp(-0.25 * (x[i] - center)**2)
            quantum_basins += amplitude * depth * (x[i]**8 - 4*x[i]**6 + 6*x[i]**4 - 4*x[i]**2 + 1)
        
        # Adaptive symmetry with quantum phase shifts
        adaptive_symmetry = 0.0
        for scale in [0.1, 0.3, 0.7, 1.2, 2.0]:
            # Add quantum delayed component
            delayed_r = np.sum(np.roll(x, self.dim//3)**2)
            phase_shift = np.sin(self.dim * np.pi / (scale + 1))
            adaptive_symmetry += np.cos(r_squared / scale) * np.sin(delayed_r / (scale + 2)) * phase_shift
        
        # Quantum noise with complex amplitude modulation
        quantum_noise = 0.0
        for i in range(self.dim):
            # Complex quantum amplitudes
            amp_real = np.sin(x[i] * (i + 1))
            amp_imag = np.cos(x[i] * (i + 2))
            quantum_noise += amp_real * amp_imag * np.tan(x[i] / (i + 4)) * np.exp(-0.1 * i)
        
        # Adaptive dimension scaling with quantum corrections
        dim_factor = 1.0 + 0.2 * np.log(self.dim + 1) + 0.1 * np.sin(self.dim * np.pi / 3) + 0.05 * np.cos(self.dim * np.pi / 5)
        
        # Quantum interference pattern
        interference = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                interference += np.sin((x[i] - x[j]) * (i + j + 1)) * np.cos((x[i] + x[j]) * (i - j + 1))
        
        return dim_factor * (0.2 * quantum_radial + 0.2 * hyper_saddle + 
                            0.2 * temporal_coupling + 0.2 * quantum_basins + 
                            0.1 * adaptive_symmetry + 0.05 * quantum_noise + 
                            0.05 * interference)